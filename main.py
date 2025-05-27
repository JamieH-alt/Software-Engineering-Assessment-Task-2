import os
from pathlib import Path
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, TabbedContent, Static, TabPane, MarkdownViewer, Collapsible, Button, Input, Label, Log, ListItem, ListView, Select, Rule
from textual.containers import Grid, VerticalScroll, Vertical, Container, Horizontal, Center
from textual.reactive import reactive
from textual.events import Event
import json
import random


# Basic Item Class for testing, Will eventually have way more stats.
class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def get_widget(self) -> Collapsible:
        return Collapsible(Static(self.description), title=self.name, collapsed=True)


# Example items in the inventory, this will later be replaced with items filled by Dnd 5E API
items = [
    Item("Sword of Testing", "A legendary test blade."),
    Item("Potion of Bugs", "Causes strange behavior."),
    Item("Scroll of Logs", "Reveals hidden logs."),
    Item("Amulet of Power", "Grants strength."),
    Item("Shield of Invincibility", "Protects from damage."),
    Item("Ring of Wisdom", "Increases intelligence.")
]



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

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value

    def delete(self, key):
         if key in self.data:
            del self.data[key]

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
        global savefilepath, savefile
        if event.item.query_one(Label).renderable == "New Save":
            self.mount(NewSaveSubmit())
        else:
            savefilepath = event.item.query_one(Label).renderable
            savefile = SaveFile(savefilepath)
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
            yield HomePage("Home (h)")

            yield MapPage("Map (m)")
            yield InventoryPage("Inventory (i)")
            yield CharacterPage("Character (c)")

            with TabPane("Help (?)", id="tab_help"):
                yield MarkdownViewer(Path("help.md").read_text(), show_table_of_contents=True)

class HomePage(TabPane): # This page is dedicated to displaying inputs
    def __init__(self, name):
        super().__init__(name, id="tab_home")

    def compose(self):
        yield Static ("Home Page", id="tab_title")
        with Horizontal(classes="home_tab-main"):
            with Vertical(classes="home_tab-columns"):
                # Everything to do with the first column here
                yield Static("Statistics", classes="generic_tab-title")
                yield Static("Hit Points: 10", classes="home_tab-statistics-stat")
                yield Static("Armor Class: 15", classes="home_tab-statistics-stat")
                yield Static("Proficiency Bonus: 2", classes="home_tab-statistics-stat")
                yield Static("")
                yield Static("Equipped Items: ", classes="home_tab-statistics-subheading")
                with VerticalScroll(classes="home_tab-statistics-verticalscroll"):
                    for i in items: # Replace this with equipped items eventualls
                        yield i.get_widget()
            with Vertical(classes="home_tab-interactions-column"):
                with VerticalScroll(classes="home_tab-interactions-console"):
                    yield Static("Welcome to the world of Dungeons and Crawlers", classes="home_tab-interactions-console-line")
                yield Rule()
                with Center():
                    with Horizontal(classes="home_tab-command_input"):
                        yield Input(placeholder="Enter a command: ", id="home_tab-interactions-command_input", classes="home_tab-interactions-command_input-input")
                        yield Button("", id="home_tab-interactions-command_button", classes="home_tab-interactions-command_input-button")
            with Vertical(classes="home_tab-columns"):
                yield Static("Minimap", classes="generic_tab-title")

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
                    for i in range(column, len(items), 3):
                        yield items[i].get_widget()

class CharacterPage(TabPane): # This just displays all the character ifnormation for the player, like stats. Just text pretty much.
    def __init__(self, name):
        super().__init__(name, id="tab_character")

    def compose(self):
        yield Static("Character Page", id="tab_title")
        with Horizontal():
            with Vertical():
                yield Static("Stats", classes="character_tab-column_title")

                yield Static("")

                yield Static("Name: Bobathy", id="label_name", classes="character_tab-label")
                yield Static("Race: Human", id="label_human", classes="character_tab-label")
                yield Static("Class: Fighter", id="label_class", classes="character_tab-label")

                yield Static("")

                yield Static("Level: 1", id="label_level", classes="character_tab-stat")

                yield Static("")

                ability_scores = CharacterCreator().reroll_stats() # sets stats to be random as saving isn't currently used

                for stat in ability_scores:
                    yield Static(f"{stat.capitalize()}: {ability_scores[stat]}", id=f"{stat}_stat", classes="character_tab-stat")

                yield Static("")

                yield Static("Hit Points: 10")
                yield Static("Armor Class: 15")
                yield Static("Proficiency Bonus: 2")
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

    def compose(self):
        # Character Name Input
        ability_scores = self.reroll_stats()

        yield Static("Character Creator", classes="generic_tab-title")

        with Center():
            yield Input(placeholder="Enter character name", id="input_name", classes="character_creator-input")

        # Race Selection
        races = [("Human", 1), ("Orc", 2)] # this style of list allows us to set things into the dropdown and give them a weighting.
        with Center():
            yield Select(races, prompt="Select Race", id = "select_race", classes="character_creator-select") # Automatically lays the list out in a drolpdown list.

        # Class Selection
        char_classes = [("Barbarian", 1), ("Fighter", 2)]
        with Center():
            yield Select(char_classes, prompt="Select Class", id = "select_class", classes="character_creator-select")

        yield Static("")

        # Level Selection (you can later expand this to be dynamic)
        yield Static("Level: 1", id="level", classes="character_creator-stat")

        yield Static("")

        # Ability Scores Display and Roll Button
        for stat in ability_scores:
            yield Static(f"{stat.capitalize()}: {ability_scores[stat]}", id=f"{stat}_stat", classes="character_creator-stat")

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
            name = event.value
        elif event.input.id == "input_race":
            race = event.value
        elif event.input.id == "input_class":
            char_class = event.value

    def on_button_pressed(self, event: Button.Pressed):
        if (event.button.id == "save_button"):
            # Save Here
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
        return ability_scores


    def roll_stat(self) -> int: # Emulates rolling 4d6 and getting rid of the lowest dice roll.
        dice = [random.randint(1, 6) for _ in range(4)]
        dice.remove(min(dice))  # Remove the lowest roll
        return sum(dice)  # Sum the remaining 3 dice


class MyApp(App): # This is the main app container that composes everything
    TITLE = "Dungeons And Critters"
    SUB_TITLE = "Version 1.0 (WIP)"
    CSS_PATH = "textual-main.tcss"
    BINDINGS = [("h", "tab_home", "Home"), ("m", "tab_map", "Map"), ("i", "tab_inventory", "Inventory"), ("c", "tab_character", "Character"), ("?", "tab_help", "Help")]

    def compose(self) -> ComposeResult: # Displays load screen before the main pages
        yield Header()
        yield LoadScreen()  # Display save/load screen first
        # yield MainPages()

    def load_game(self) -> None: 
        self.query_one(LoadScreen).remove()  # Remove the save/load screen
        self.mount(MainPages())  # Show the main app after loading

    def load_made_game(self) -> None: # The game is made so it gets rid of the character creator.
        self.query_one(CharacterCreator).remove()
        self.mount(MainPages())

    def create_game(self) -> None: # This loads the character creator
        self.query_one(LoadScreen).remove()
        self.mount(CharacterCreator())

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
    app = MyApp()
    app.run()