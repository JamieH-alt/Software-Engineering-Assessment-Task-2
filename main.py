import os
from pathlib import Path
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, TabbedContent, Static, TabPane, MarkdownViewer, Collapsible, Button, Input, Label, Log, ListItem, ListView, Select, ProgressBar, Rule
from textual.containers import Grid, VerticalScroll, Vertical, Container, Horizontal, Center
from textual.reactive import reactive
from textual.events import Event
from textual.message import Message
import json
import random
import class_segregation as cs
import item as it
import terminal as term

# Updated List with All Classes

items = it.items

# These maps allow for Items to be easily found from the index
item_map = {item.index: item for item in items}
Log(item_map)

savefilepath = ""
savefile = None

class SaveFile(): # This is a basic non-saving save file system, It does load but doesn't save.
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = {}
        self.load()

    def load(self): # Try's to read the file but if it fails returns null.
        try:
            with open(self.filepath, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}


    def save(self): # Unused but this would theoretically save the file (Unused because nothing is added to the save data yet)
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f, indent=4)

    def get_player(self):
        return self.data.get("player", None)

    def set_player(self, player_data):
        self.data["player"] = player_data
        self.save()


class NewSaveSubmit(Horizontal): # This is the button submit and the input for save files. This allows us to send the player to the character menu
    def __init__(self):
        super().__init__(classes="load_screen-submit")
        self.savename = ""

    def on_input_changed(self, event: Input.Changed):
        self.savename = ''.join(e for e in event.value if e.isalnum())

    def on_button_pressed(self, event: Button.Pressed):
        global savefilepath, savefile
        if event.button.id == "submit_button": # Makes sure its the correct button
            savefiles = []

            for entry in os.scandir("saves"):
                if entry.is_file() and Path(entry).suffix == ".json":
                    savefiles.append(entry.path)


            if len(savefiles) != 0 and "saves/" + self.savename + ".json" in savefiles:
                return

            savefilepath = "saves/" + self.savename + ".json"

            savefile = SaveFile(savefilepath)

            self.app.create_game()

    def compose(self): # This is just setting up what is inside of the Horizontal frame
        yield Input(placeholder="Save Name", classes="load_screen-input")
        yield Button(label="Submit", id="submit_button", classes="load_screen-button")

class LoadScreen(Container): # This lists of every save in a ListView and then adds an extra iteration for the new save.
    def __init__(self):
        super().__init__()
        directory = "saves"
        self.savefiles = []

        for entry in os.scandir(directory):
            if entry.is_file() and Path(entry).suffix == ".json":
                self.savefiles.append(entry.path)

    def on_list_view_selected(self, event: ListView.Selected):
        global savefilepath, savefile, cs
        if event.item.query_one(Label).renderable == "New Save":
            self.mount(NewSaveSubmit())
        else:
            savefilepath = "saves/" + event.item.query_one(Label).renderable + ".json"
            savefile = SaveFile(savefilepath)
            player_data = savefile.get_player()
            if player_data:
                cs.player = cs.Player(
                    name=player_data["name"],
                    race=cs.Race.from_id(player_data["race_id"]),
                    charclass=cs.CharClass.from_id(player_data["class_id"]),
                    stats=cs.Stats(**player_data["stats"]),
                    hitpoints=player_data["hitpoints"],
                    armorclass=player_data["armorclass"],
                    proficiencybonus=player_data["proficiencybonus"],
                    spells=player_data["spells"],
                    inventory=[item_map[i] for i in player_data["inventory"]],
                    equipped_inventory=[item_map[i] for i in player_data["equipped_inventory"]]
                )

                cs.player.level = cs.Level(player_data["level"])
                cs.player.level.currentexp = player_data["currentexp"]
                cs.player.currencypoints = player_data["currencypoints"]
                cs.player.set_health(player_data.get("health", player_data["hitpoints"]))
                cs.player.set_max_health(player_data.get("max_health", player_data["hitpoints"]))
            self.app.load_game()

    def compose(self):
        yield Static("Select Save", id="tab_title")
        with ListView(id="save_item"):
            if len(self.savefiles) != 0:
                for save in self.savefiles:
                    yield ListItem(Label(save.lstrip("saves/").rstrip(".json")))
            yield ListItem(Label("New Save"))

class MainPages(Container): # This is the main container for the app that sets up all the pages
    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        global items

        with TabbedContent(): # This allows us to have tabs to break up the program into various windows
            home = HomePage("Home (h)")
            home.health = cs.player.get_health()
            home.max_health = cs.player.get_max_health()
            home.currencypoints = cs.player.get_currencypoints()
            yield home

            yield MapPage("Map (m)")
            yield InventoryPage("Inventory (i)")
            character = CharacterPage("Character (c)")
            character.health = cs.player.get_health()
            character.max_health = cs.player.get_max_health()
            character.armour_class = cs.player.get_armorclass()
            character.currencypoints = cs.player.get_currencypoints()
            character.exp = cs.player.level.get_current_exp()
            character.level = cs.player.level.get_level()
            yield character

            with TabPane("Help (?)", id="tab_help"):
                yield MarkdownViewer(Path("help.md").read_text(), show_table_of_contents=True)


class HomePage(TabPane): # This page is dedicated to displaying inputs

    health = reactive(0)
    max_health = reactive(0)
    armour_class = reactive(0)
    currencypoints = reactive(0)

    def __init__(self, name):
        super().__init__(name, id="tab_home")
        self.scroll = VerticalScroll(Static("Welcome to Dungeons and Crawlers!", classes="home_tab-interactions-console-line"), Static("T -:--", id="home_tab-interactions-console-timer", classes="home_tab-interactions-console-timer"), classes="home_tab-interactions-console")
        self.grid = Grid()
        self.health = self.app.player._health
        self.max_health = self.app.player._max_health
        self.armour_class = self.app.player.get_armorclass()

    def watch_health(self, old_health: int, new_health: int):
        try:
            self.query_one("#health_static").update(f"Health: {new_health}/{self.max_health}")
        except:
            print("")

    def watch_max_health(self, old_max_health: int, new_max_health: int):
        try:
            self.query_one("#health_static").update(f"Health: {self.health}/{new_max_health}")
        except:
            print("")

    def watch_armour_class(self, old_armour_class: int, new_armour_class: int):
        try:
            self.query_one("#armour_class_static").update(f"Armor Class: {new_armour_class}")
        except:
            print("")

    def watch_currencypoints(self, old_currencypoints: int, new_currencypoints: int):
        try:
            self.query_one("#moneybagcontainer").remove_children()
            self.query_one("#moneybagcontainer").mount(Static("Money Bag: ", classes="generic-money_bag-item"))
            cost2 = cs.Cost.translate_from_currency_ponts(new_currencypoints)
            for key in cost2:
                self.query_one("#moneybagcontainer").mount(Static(str(cost2[key]), classes="generic-money_bag-item"))
                style = Static(key)
                style.styles.color = cs.costcolours.get(key, "white")
                self.query_one("#moneybagcontainer").mount(style)
            if cost2 == {}:
                self.query_one("#moneybagcontainer").mount(Static("No Money", classes="generic-money_bag-item"))
        except:
            print("")

    def compose(self):
        yield Static ("Home Page", id="tab_title")
        with Horizontal(classes="home_tab-main"):
            with Vertical(classes="home_tab-columns"):
                # Everything to do with the first column here
                yield Static("Statistics", classes="generic_tab-title")
                yield Static(f"{self.app.player._name}", classes="generic_tab-title")
                yield Static(f"Health: {self.health}/{self.max_health}", classes="home_tab-statistics-stat", id="health_static")
                yield Static(f"Armor Class: {self.armour_class}", classes="home_tab-statistics-stat", id="armour_class_static")
                yield Static(f"Proficiency Bonus: {self.app.player.get_proficiencybonus()}", classes="home_tab-statistics-stat")
                yield Rule()
                cost2 = cs.Cost.translate_from_currency_ponts(cs.player.currencypoints)
                with Horizontal(classes="generic-money_bag", id="moneybagcontainer"):
                    yield Static(f"Money Bag: ", classes="generic-money_bag-item")
                    for key in cost2:
                        yield Static(str(cost2[key]), classes="generic-money_bag-item")
                        style = Static(key)
                        style.styles.color = cs.costcolours.get(key, "white")
                        yield style
                    if cost2 == {}:
                        yield Static("No Money", classes="generic-money_bag-item")
                yield Rule()
                yield Static("Equipped Items: ", classes="home_tab-statistics-subheading")
                with VerticalScroll(classes="home_tab-statistics-verticalscroll", id="equipped_items_container"):
                    for i in cs.player.equipped_inventory: # Replace this with equipped items eventualls
                        yield i.get_widget(cs.player)
            with Vertical(classes="home_tab-interactions-column"):
                yield self.scroll
                yield Rule()
                with Center():
                    with Horizontal(classes="home_tab-command_input"):
                        yield Input(placeholder="Enter a command: ", id="home_tab-interactions-command_input", classes="home_tab-interactions-command_input-input")
                        yield Button("", id="home_tab-interactions-command_button", classes="home_tab-interactions-command_input-button")
            with Vertical(classes="home_tab-columns", id="minimapcontainer"):
                yield Static("Minimap", classes="generic_tab-title")
                yield Static(f"Town: {self.app.town.name}", classes="generic_tab-title")
                self.grid = self.app.grid_view
                self.app.grid_view = self.grid
                self.app.grid_initialised = True
                yield self.grid

    def on_mount(self):
        self.app.grid_initialised = True
        self.grid = self.app.grid_view
        self.app.grid_view = self.grid
        self.grid.update_view()
                

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "home_tab-interactions-command_button":
            if event.button.parent.query_children("Input").first().value == "":
                return
            self.handle_command(event.button.parent.query_children("Input").first().value)
            event.button.parent.query_children("Input").first().value = ""

    def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.value == "":
            return
        
        self.handle_command(event.value)

        event.input.value = ""
        

    def handle_command(self, command) -> None:
        self.terminal_message(f"{cs.player._name} >> {command}")

        command = command.lower()
        player = cs.player
        player_tile = self.app.playertile

        if command.split(" ")[0] == "travel":
            if command.split(" ")[1] == "1":
                self.app.map = term.LocationMap(term.shorecliffs_tiles())
                player_tile.x = 6
                player_tile.y = 6
                self.app.grid_view = term.TownView(player_tile, self.app.map)
                self.app.grid_view.can_focus = True
                self.app.grid_initialised = True
                self.grid = self.app.grid_view
                self.app.grid_view = self.grid
                self.query_one("#minimapcontainer").remove_children()
                self.query_one("#minimapcontainer").mount(Static("Minimap", classes="generic_tab-title"))
                self.query_one("#minimapcontainer").mount(Static(f"Town: {self.app.town.name}", classes="generic_tab-title"))
                self.query_one("#minimapcontainer").mount(self.grid)

        # Handle building commands
        if player_tile.current_building:
            if player_tile.current_building.type == 'inn':
                player_tile.current_building.rest(player, self.app.grid_view)
            elif player_tile.current_building.type == 'blacksmith' and command.startswith('buy '):
                item_name = command[4:].strip()
                player_tile.current_building.buy_item(player, item_name, self.app.grid_view)
            else:
                self.terminal_message(f"Unknown command: {command}")
            self.app.grid_view.focus()
        
                
    def refresh_content(self):
        container = self.query_one("#equipped_items_container")
        container.remove_children()
        for item in cs.player.equipped_inventory:
            widget = item.get_widget(cs.player)
            widget._watch_collapsed(cs.Item.on_collapsible_toggled)
            container.mount(widget)

    def terminal_message(self, message: str):
        # Mounting new messages in the inner container appends them underneath previously added messages
        self.scroll.mount(
            Static(message, classes="home_tab-interactions-console-line")
        )

        # Check the command here
        Log("TODO: Log Command Here")
    
    def terminal_rule(self):
        self.scroll.mount(
            Rule()
        )
    

class MapPage(TabPane): # Self explanatory, just text and columns aswell as an ascii art of what the map might look like.
    def __init__(self, name):
        super().__init__(name, id="tab_map")

    def compose(self):
        yield Static("Map Page", id="tab_title")
        ascii_art = r"""

                                  ~~~~~~
                        /\       ~~~~~~~     OAKENSHORE
                   /\  /__\       ~~~        (City of Oaks)
                 /\   /    \         ~~~~
              /\ /__\        /\       ~~~~~~~
             /__\            /__\     ~~~~~~~
            /\   VALLEY OF THE KINGS         /\\
           /__\          /\                 /__\\
                 /\     /__\              FOOTHILLS
                /__\                    (Small Town)
                   RIVER OF DRAGONS   ~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~                        ~~~~~~~~
~~~~~~~~~~~~~~         MOUNT ASHBRIAR     ~~~~~~~~
    ~~~~~~~~~~~~~~          /\            ~~~~~~~~~~~
~~~~~~~~~~                 /__\                 ~~~~~~~
~                     /\                       HIGHLANDS
~    WINDWOOD     ~~~/  \~~~           VALORSTED (Capital)
~   (Dense Forest)~~~    ~~~~          ~~~~~~~~~~~~~~~
~~~~~    ~~~~~~~~~~~    ~~~~~~~~       ~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~       ~~~~~~~~~~        ~~~~
                     SHORECLIFFS         ~~~~~~~~~
                           (Coastal City)                   """
        # Create a Static widget with the ASCII art
        with Horizontal():
            asciiartmap = Static(ascii_art, classes="map_tab-ascii")
            asciiartmap.border_title="Elednor Isles"
            yield asciiartmap
            with Vertical(classes = "map_tab-column"):
                yield Static("Some info over here or smth", classes="map_tab-sub_info")
                yield Static("* ELednor Isles 15 anno", classes="map_tab-sub_info")
                yield Static("* Other basic info", classes="map_tab-sub_info")

class InventoryPage(TabPane): # This just loops through all the items that are in the items list and puts them into a grid for the user, allowing them to be dropped down with the .get_widget from  the Item() class
    def __init__(self, name):
        super().__init__(name, id="tab_inventory")

    def compose(self):
        yield Static("Inventory Page", id="tab_title")
        with Grid(id="inventory_grid"):
            for column in range(3):
                with VerticalScroll(id=f"inventory_column_{column}"):
                    for i in range(column, len(cs.player.inventory), 3):
                        yield cs.player.inventory[i].get_widget(cs.player)
        self.refresh_content()

    def refresh_content(self):
        try:
            for column in range(3):
                container1 = self.query_one("#inventory_grid")
                container = container1.query_one(f"#inventory_column_{column}")
                container.remove_children()
                for item in range(column, len(cs.player.inventory), 3):
                    widget = cs.player.inventory[item].get_widget(cs.player)
                    widget._watch_collapsed(cs.Item.on_collapsible_toggled)
                    container.mount(widget)
        except:
            print("--- This is an okay error. ---")

class CharacterPage(TabPane): # This just displays all the character ifnormation for the player, like stats. Just text pretty much.

    health = reactive(0)
    max_health = reactive(0)
    armour_class = reactive(0)
    currencypoints = reactive(0)
    level = reactive(0)
    exp = reactive(0)
    stats = reactive(False)

    def __init__(self, name):
        super().__init__(name, id="tab_character")

    #     self.level = cs.player.level.get_level()
    #     self.exp = cs.player.level.get_current_exp()
    #     self.max_exp = cs.player.level.required_exp(self.level + 1)

    def watch_health(self, old_health: int, new_health: int):
        try:
            self.query_one("#health_static").update(f"Health: {new_health}/{self.max_health}")
        except:
            print("")

    def watch_max_health(self, old_max_health: int, new_max_health: int):
        try:
            self.query_one("#health_static").update(f"Health: {self.health}/{new_max_health}")
        except:
            print("")

    def watch_armour_class(self, old_armour_class: int, new_armour_class: int):
        try:
            self.query_one("#armour_class_static").update(f"Armor Class: {new_armour_class}")
        except:
            print("")

    def watch_currencypoints(self, old_currencypoints: int, new_currencypoints: int):
        try:
            self.query_one("#moneybagcontainer").remove_children()
            self.query_one("#moneybagcontainer").mount(Static("Money Bag: ", classes="generic-money_bag-item"))
            cost2 = cs.Cost.translate_from_currency_ponts(new_currencypoints)
            for key in cost2:
                self.query_one("#moneybagcontainer").mount(Static(str(cost2[key]), classes="generic-money_bag-item"))
                style = Static(key)
                style.styles.color = cs.costcolours.get(key, "white")
                self.query_one("#moneybagcontainer").mount(style)
            if cost2 == {}:
                self.query_one("#moneybagcontainer").mount(Static("No Money", classes="generic-money_bag-item"))
        except:
            print("")

    def watch_level(self, old_level: int, new_level: int):
        try:
            self.query_one("#level_static").update(f"Level: {new_level} ({cs.player.level.get_current_exp()}/{cs.player.level.required_exp(cs.player.level.level + 1)})")
            self.stats = False if self.stats else True
        except:
            print("")
    
    def watch_exp(self, old_exp: int, new_exp: int):
        try:
            if new_exp != 0:
                self.query_one("#exp_progress_bar").advance(new_exp - old_exp)
        except:
            print("")

    def watch_stats(self, old_stats: bool, new_stats: bool):
        try:
            ability_scores = cs.player.get_stats().to_dict()
            for stat in ability_scores:
                self.query_one(f"#{stat}_stat").update(f"{stat.capitalize()}: {ability_scores[stat]}")
        except:
            print("")

    def compose(self):
        yield Static("Character Page", id="tab_title")
        with Horizontal():
            with Vertical():
                yield Static("Stats", classes="character_tab-column_title")

                yield Static("")

                yield Static(f"Name: {cs.player._name}", id="label_name", classes="character_tab-label")
                yield Static(f"Race: {cs.player.get_race().get_name()}", id="label_human", classes="character_tab-label")
                yield Static(f"Class: {cs.player.get_class().get_name()}", id="label_class", classes="character_tab-label")

                yield Static("")

                yield Static(f"Level: {cs.player.level.get_level()} ({cs.player.level.get_current_exp()}/{cs.player.level.required_exp(cs.player.level.level + 1)})", id="level_static", classes="character_tab-stat")
                progressbar = ProgressBar(total=cs.Level.required_exp(cs.player.level.get_level() + 1), show_eta=False, show_percentage=True, id="exp_progress_bar")
                progressbar.advance(cs.player.level.get_current_exp())
                yield progressbar

                yield Static("")

                ability_scores = cs.player.get_stats().to_dict() # sets stats to be random as saving isn't currently used

                for stat in ability_scores:
                    yield Static(f"{stat.capitalize()}: {ability_scores[stat]}", id=f"{stat}_stat", classes="character_tab-stat")

                yield Static("")

                yield Static(f"Health: {cs.player.get_health()}", id="health_static")
                yield Static(f"Armor Class: {cs.player.get_armorclass()}", id="armour_class_static")
                yield Static("Proficiency Bonus: 2")

                yield Static("")

                cost2 = cs.Cost.translate_from_currency_ponts(cs.player.currencypoints)
                with Horizontal(classes="generic-money_bag", id="moneybagcontainer"):
                    yield Static(f"Money Bag: ", classes="generic-money_bag-item")
                    for key in cost2:
                        yield Static(str(cost2[key]), classes="generic-money_bag-item")
                        style = Static(key)
                        style.styles.color = cs.costcolours.get(key, "white")
                        yield style
                    if cost2 == {}:
                        yield Static("No Money", classes="generic-money_bag-item")
            with Vertical():
                yield Static("Spells", classes="character_tab-column_title")

                yield Static("")

                yield Static("* You have no spells")
            with Vertical():
                yield Static("Others", classes="character_tab-column_title")

                yield Static("")

                yield Static("* Nothing to See Here")

class CharacterCreator(Container): # Creates the character
    def __init__(self):
        super().__init__(id="character_creator-main")
        self.ability_scores = self.reroll_stats()
        self.char_name = "John Doe"
        self.race = cs.Human
        self.char_class = cs.Barbarian

    def compose(self):
        # Character Name Input
        yield Static("Character Creator", classes="generic_tab-title")

        with Center():
            yield Input(placeholder="Enter character name", id="input_name", classes="character_creator-input")

        # Race Selection
        races = []
        for i in cs.Races:
            races.append((i.get_name(), i.get_id()))
        with Center():
            yield Select(races, prompt="Select Race", id = "select_race", classes="character_creator-select") # Automatically lays the list out in a drolpdown list.

        # Class Selection
        charclasses = []
        for i in cs.Classes:
            charclasses.append((i.get_name(), i.get_id()))
        with Center():
            yield Select(charclasses, prompt="Select Class", id = "select_class", classes="character_creator-select")

        yield Static("")

        # Level Selection (you can later expand this to be dynamic)
        yield Static("Level: 1", id="level", classes="character_creator-stat")

        yield Static("")

        # Ability Scores Display and Roll Button
        for stat in self.ability_scores:
            yield Static(f"{stat.capitalize()}: {self.ability_scores[stat]}", id=f"{stat}_stat", classes="character_creator-stat")

        yield Static("")

        with Center():
            yield Button(label="Roll Ability Scores", id="roll_button", classes="character_creator-roll_button")

        yield Static("")

        # Hit Points Input
        yield Static("Hit Points: 10", id="label_hp", classes="character_creator-stat")

        # Armor Class Input
        yield Static("Armor Class: 15", id="label_ac", classes="character_creator-stat")

        # Proficiency Bonus Input
        yield Static("Proficiency Bonus: 2", id="label_pb", classes="character_creator-stat")

        yield Static("")

        # Final confirmation or save button
        with Center():
            yield Button(label="Create Character", id="save_button", classes="character_creator-save_button")

    def on_input_changed(self, event: Input.Changed):
        """Handle all input changes in one function"""
        if event.input.id == "input_name":
            self.char_name = event.value
    
    def on_select_changed(self, event: Select.Changed):
        if event.select.id == "select_race":
            self.race = cs.Race.from_id(event.value)
        elif event.select.id == "select_class":
            self.char_class = cs.CharClass.from_id(event.value)


    def on_button_pressed(self, event: Button.Pressed):
        if (event.button.id == "save_button"):
            cs.player = cs.Player(
                name=self.char_name,
                race=self.race,
                charclass=self.char_class,
                stats=cs.Stats(self.ability_scores["strength"], self.ability_scores["dexterity"], self.ability_scores["constitution"], self.ability_scores["intelligence"], self.ability_scores["wisdom"], self.ability_scores["charisma"]),
                hitpoints=10,
                armorclass=15,
                proficiencybonus=2,
                spells=[],
                inventory=[it.Greatsword],
                equipped_inventory=[]
            )

            cs.player.set_currencypoints(245)

            cs.player.set_health(10)
            cs.player.set_max_health(20)

            if savefile:
                savefile.set_player(cs.player.serialize())

            self.app.load_made_game()
        elif (event.button.id == "roll_button"):
            ability_scores = self.reroll_stats()
            for key in ability_scores:
                self.query_one(f"#{key}_stat", Static).update(f"{key.capitalize()}: " + str(ability_scores[key]))

    def reroll_stats(self): # Randomises stats
        ability_scores = {}
        ability_scores["strength"] = self.roll_stat()
        ability_scores["dexterity"] = self.roll_stat()
        ability_scores["constitution"] = self.roll_stat()
        ability_scores["intelligence"] = self.roll_stat()
        ability_scores["wisdom"] = self.roll_stat()
        ability_scores["charisma"] = self.roll_stat()
        self.ability_scores = ability_scores
        return ability_scores


    def roll_stat(self) -> int: # Emulates rolling 4d6 and getting rid of the lowest dice roll.
        dice = [random.randint(1, 6) for _ in range(4)]
        dice.remove(min(dice))  # Remove the lowest roll
        return sum(dice)  # Sum the remaining 3 dice


class MyApp(App): # This is the main app container that composes everything
    TITLE = "Dungeons And Critters"
    SUB_TITLE = "Version 1.0 (WIP)"
    CSS_PATH = "textual-main.tcss"
    BINDINGS = [("h", "tab_home", "Home"), ("m", "tab_map", "Map"), ("i", "tab_inventory", "Inventory"), ("c", "tab_character", "Character"), ("?", "tab_help", "Help"),
                ("left", "move('left')", "Move Left"),
                ("right", "move('right')", "Move Right"),
                ("up", "move('up')", "Move Up"),
                ("down", "move('down')", "Move Down")]

    def __init__(self):
        super().__init__()
        self.map = term.LocationMap(term.oakenshore())
        self.playertile = term.PlayerTile(6, 6)
        self.playertile.app = self
        self.grid_view = term.TownView(self.playertile, self.map)
        self.grid_view.can_focus = True
        self.town = term.create_oakenshore(self.playertile, self.map)
        self.grid_initialised = False
        self.player = cs.player

    def compose(self) -> ComposeResult: # Displays load screen before the main pages
        yield Header()
        yield LoadScreen()  # Display save/load screen first
        # yield MainPages()

    def action_move(self, direction: str):
        if self.grid_initialised:
            self.playertile.move(direction, self.map, self.town)
            self.grid_view.update_view()

    def load_game(self) -> None: 
        self.query_one(LoadScreen).remove()  # Remove the save/load screen
        self.mount(MainPages())  # Show the main app after loading
        # Load the reactive stats

    def load_made_game(self) -> None: # The game is made so it gets rid of the character creator.
        self.query_one(CharacterCreator).remove()
        self.mount(MainPages())

    def create_game(self) -> None: # This loads the character creator
        self.query_one(LoadScreen).remove()
        self.mount(CharacterCreator())

    def save_game(self):
        global savefile, cs
        if savefile and hasattr(cs, 'player'):
            savefile.set_player(cs.player.serialize())

    def on_exit(self):
        self.save_game()
    
    def on_tabbed_content_tab_activated(self, event: TabbedContent.TabActivated) -> None:
        if event.tab.id == "Tab_inventory":
            event.tab.refresh_content()
        elif event.tab.id == "tab_home":
            event.tab.refresh_content()
        elif event.tab.id == "tab_character":
            event.tab.refresh_content()

    # This sets up all of the tabs
    def action_tab_home(self) -> None:
        self.query_one(TabbedContent).active = "tab_home"
    def action_tab_map(self) -> None:
        self.query_one(TabbedContent).active = "tab_map"

    def action_tab_inventory(self) -> None:
        self.query_one(TabbedContent).active = "tab_inventory"

    def action_tab_character(self) -> None:
        self.query_one(TabbedContent).active = "tab_character"

    def action_tab_help(self) -> None:
        self.query_one(TabbedContent).active = "tab_help"


if __name__ == "__main__":
    if not os.path.exists("saves"):
        os.makedirs("saves")
    app = MyApp()
    app.run()