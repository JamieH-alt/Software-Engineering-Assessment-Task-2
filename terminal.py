# This file is dedicated to the terminal system. And will probably be huge.
"""
This game will have 2 main states.
Inside Location.
Outside Location.

Inside Location will involve moving the player around a town, buying stuff etc... This will be mainly handled using a Location() tab.
Outside Location will involve moving the player between towns, and will be how the game starts off. It will ask the player where they want to go (Look at the ascii map for reference)

The outside location travel will be timed! --- Maybe add a random chance for attacks

Inside location will have 2 different types of locations
Dungeon
Town

Towns will just be for the player to walk around and show in.

Dungeons will be a text based combat sim.
"""
from textual.app import App, ComposeResult
from textual.widgets import Static, Log
from textual.containers import Grid
from textual.reactive import reactive
from textual import events
import class_segregation as cs
import item
import random

# This is all focused on the MiniMap and it's loading system ( For Towns and Dungeons )

class TileWidget(Static):
    def __init__(self, char: str, TILE_COLORS: dict):
        super().__init__(char, classes="terminal-tile")
        # This here is the movement system basis.
        self.TILE_COLORS = TILE_COLORS
        self.char = char
        self.update(char)
        self.styles.color = self.TILE_COLORS.get(char, "white")
    
    def set_char(self, char: str):
        self.char = char
        self.update(char)
        self.styles.color = self.TILE_COLORS.get(char, "white")
    
class LocationMap:
    def __init__(self, tiles):
        self.width = len(tiles[0])
        self.height = len(tiles)
        self.tiles = tiles

    def get_tile(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]
        return " "
    
    def is_walkable(self, x, y):
        return self.get_tile(x, y) == "R" or self.get_tile(x, y) == "G"
    
    def is_enterable(self, x, y):
        return self.get_tile(x, y) in ["A", "B", "I"]

    def is_exit(self, x, y):
        return self.get_tile(x, y) == "E"
    
class PlayerTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.current_building = None
    
    def move(self, direction: str, game_map: LocationMap, town: 'Town'):
        dx, dy = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}.get(direction, (0, 0))
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < game_map.width and 0 <= new_y < game_map.height:
            if game_map.is_walkable(new_x, new_y):
                self.x = new_x
                self.y = new_y
            elif game_map.is_enterable(new_x, new_y):
                building = town.get_building_at(new_x, new_y)
                if building:
                    self.current_building = building
                    self.handle_building_interaction(building, town.townview)
            elif game_map.is_exit(new_x, new_y):
                self.handle_exit_interaction(town.townview)
            else:
                # Play sound here
                Log("TODO Play Sound System")
    
    def handle_exit_interaction(self, location_view):
        app = location_view.app
        home_tab = app.query_one("#tab_home")
        home_tab.terminal_message("You can travel to the following towns: ")
        home_tab.terminal_message("1. Shorecliffs")
        home_tab.terminal_message("2. Foothills")
        home_tab.terminal_message("3. Highlands Valor")
        home_tab.terminal_message("4. Oakenshore")
        home_tab.terminal_message("--- Dungeons ---")
        home_tab.terminal_message("5. Windwood Dungeon (E-Class)")
        home_tab.terminal_message(">> Type: Travel (number here)")
        home_tab.terminal_message("Example: Travel 1")
        location_view.exit()

    @staticmethod
    def travel_message(app):
        home_tab = app.query_one("#tab_home")
        home_tab.terminal_message("You can travel to the following towns: ")
        home_tab.terminal_message("1. Shorecliffs")
        home_tab.terminal_message("2. Foothills")
        home_tab.terminal_message("3. Highlands Valor")
        home_tab.terminal_message("4. Oakenshore")
        home_tab.terminal_message("--- Dungeons ---")
        home_tab.terminal_message("5. Windwood Dungeon (E-Class)")
        home_tab.terminal_message(">> Type: Travel (number here)")
        home_tab.terminal_message("Example: Travel 1")

    def handle_building_interaction(self, building, location_view):
        app = location_view.app
        home_tab = app.query_one("#tab_home")
        
        if building.type == 'inn':
            home_tab.terminal_rule()
            home_tab.terminal_message(f"You enter {building.name}")
            home_tab.terminal_message(building.description)
            home_tab.terminal_message(f"Type 'rest' to heal for {building.healing_amount} HP")
        elif building.type == 'blacksmith':
            home_tab.terminal_rule()
            home_tab.terminal_message(f"You enter {building.name}")
            home_tab.terminal_message(building.description)
            building.show_items(location_view)
        elif building.type == 'guild':  # Handle Adventurers Guild
            home_tab.terminal_rule()
            home_tab.terminal_message(f"You enter {building.name}")
            home_tab.terminal_message(building.description)
            home_tab.terminal_message("Greetings adventurer! We don't have any quests available!")

def oakenshore():
    layout = [
    "XXXXXXXXXXXXXX",
    "XXXRRRXXXXXRRX",
    "XGGGRRRXXRRGGX",
    "XGRRRRRRRRRRRX",
    "XGIRRRRRRRRRGX",
    "XGRRRRRRRRRGGX",
    "XGGGRRRRRRAGGX",
    "XGRRRRRRRGGGGX",
    "XGGBRRRRRRRGGX",
    "XXRGRRRRRRGGGX",
    "XGGRRRRRRRGGGX",
    "XXXRRRRRRRXXXX",
    "XXXRRRRRRXXXXX",
    "XXXXXEEEEXXXXX"
    ]
    return [list(row) for row in layout]

def shorecliffs_tiles():
    layout = [
        "XXXXXXXXXXXXXX",
        "XRRRRRRRRRRRRX",
        "XRGGRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XBRRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRIX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRARX",
        "XXXXXXEEXXXXXX"
    ]
    return [list(row) for row in layout]

def foothills_tiles():
    layout = [
        "XXXXXXXXXXXXXX",
        "XRRRRRRRRRIRRX",
        "XRRRRRRRRRRRRX",
        "XBRRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRAX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XXXXXXEEXXXXXX"
    ]
    return [list(row) for row in layout]

def highlands_valor_tiles():
    layout = [
        "XXXXXXXXXXXXXX",
        "XRRRRRRRRRRRRX",
        "XARRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRIX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XRRRRRRRRRRRRX",
        "XBRRRRRRRRRRRX",
        "XXXXXXEEXXXXXX"
    ]
    return [list(row) for row in layout]

def create_oakenshore(playertile: PlayerTile, game_map: LocationMap) -> 'Town':
    inn = Inn("The Sleeping Dragon Inn", 2, 4, "I",
              "A Cozy inn with warm beds and healthy meals",
              15, 10)
    blacksmith = Blacksmith("Ironforge Armory", 3, 8, "B",
                            "Finest weapons and armor in the greater region",
                            [item.Shortsword, item.Chain_Mail, item.Greataxe, item.Dagger])
    adventurers_guild = Building("Adventurer's Guild", "guild", 10, 6, "A",
                                 "A gathering place for brave heroes seeking quests")
    exit = Exit(5, 13, 8, 13, "E")
    return Town("Oakenshore", "A bustling coatal town, and the city of oaks", [inn, blacksmith, adventurers_guild], exit, TownView(playertile, game_map))

def create_shorecliff_tiles(playertile: PlayerTile, game_map: LocationMap):
    inn = Inn("The Highland Fox Inn", 12, 8, "I",
              "The Inn above the Clouds and Sea",
              20, 12)
    blacksmith = Blacksmith("Ironforge Armory", 1, 5, "B",
                            "Forged in the eye of the sea",
                            [item.Longbow, item.Warhammer, item.Spear, item.Splint_Armor])
    adventures_guild = Building("Adventurer's Guild", "guild", 11, 12, "A",
                                "Shorecliff Branch - A gathering place for brave heroes seeking quests!")
    exit = Exit(6, 13, 7, 13, "E")
    return Town("Shorecliff", "A futuristic town above the sea in the highlands", [inn, blacksmith, adventures_guild], exit, TownView(playertile, game_map))

def create_foothills_tiles(playertile: PlayerTile, game_map: LocationMap):
    inn = Inn("Foothills Inn", 10, 1, "I",
              "Sleep tight",
              20, 20)
    blacksmith = Blacksmith("Hilly Smithy", 1, 3, "B",
                            "Made in the hilly meadows of Elednor",
                            [item.Bedroll, item.Battleaxe, item.Spike_iron, item.Small_knife])
    adventurers_guild = Building("Adventurer's Guild", "guild", 12, 10, "A",
                                 "Foothills Branch - A gathering place for brave heroes seeking quests!")
    exit = Exit(6, 13, 7, 13, "E")
    return Town("Foothills", "A small meadow-bound town of Elednor", [inn, blacksmith, adventurers_guild], exit, TownView(playertile, game_map))

def create_highlands_valor_tiles(playertile: PlayerTile, game_map: LocationMap):
    inn = Inn("Highlands Valor's Soul", 12, 4, "I",
              "The soul of the truest highlands of Elednor",
              40, 30)
    blacksmith = Blacksmith("Passionate Makers", 1, 12, "B",
                            "Forged in the passionate flame of a dwarf's heart",
                            [item.Dagger, item.Small_knife, item.Light_hammer, item.Mace])
    adventurers_guild = Building("Adventurer's guild", "guild", 1, 2, "A",
                                 "Highlands Valor Branch - A gathering place for brave heroes seeking quests!")
    exit = Exit(6, 13, 7, 13, "E")
    return Town("Highlands Valor", "The truest highlands of Elednor", [inn, blacksmith, adventurers_guild], exit, TownView(playertile, game_map))

# This is the 7x7 display around the player
class LocationView(Grid):

    def __init__(self, player: PlayerTile, game_map: LocationMap):
        super().__init__(id="minimap_view")
        self.player = player
        self.game_map = game_map
        self.cells = []
        self.available = 1 # This will be set to available when the player is ACTUALLY at a location
        self.TILE_COLORS = {
            "P": "white", #Player
            "R": "#8c5740", # Road
            "G": "#476850", # Dirt
            "X": "grey", # Wall
            " ": "black", #Empty / Out of bounds area
            "E": "#ffa840" # Exit
        }
    
    def compose(self) -> ComposeResult:
        if self.available == 0:
            yield Static("N/A")
        else:
            half = 14 // 2
            for dy in range(-half, half + 1):
                for dx in range(-half, half + 1):
                    tile = TileWidget(" ", self.TILE_COLORS)
                    self.cells.append(tile)
                    yield tile
    
    def update_view(self):
        if self.available == 0:
            self.remove_children()
            self.mount(Static("N/A"))
        half = 14 // 2
        for dy in range(-half, half + 1):
            for dx in range(-half, half + 1):
                x = self.player.x + dx
                y = self.player.y + dy
                char = "P" if dx == 0 and dy == 0 else self.game_map.get_tile(x, y)
                index = (dy + half) * 14 + (dx + half)
                self.cells[index].set_char(char)
    
    def exit(self):
        self.available = 0
        minimap_container = self.app.query_one("#minimapcontainer")
        minimap_container.remove_children()
        minimap_container.mount(Static("Minimap", classes="generic_tab-title"))
        minimap_container.mount(Static(f"Town: ---", classes="generic_tab-title"))
    
    @staticmethod
    def enter(app: App, player: PlayerTile, game_map: LocationMap):
        container = app.query_one("#minimapcontainer")
        container.mount(LocationView(player, game_map))

class TownView(LocationView):
    def __init__(self, player: PlayerTile, game_map: LocationMap):
        super().__init__(player, game_map)
        self.TILE_COLORS["I"] = "#95d8ae" # Inn
        self.TILE_COLORS["A"] = "#e7a0bd" # Adventurers Guild
        self.TILE_COLORS["B"] = "#95d8ae" # Blacksmith

    def exit(self):
        self.available = 0
        minimap_container = self.app.query_one("#minimapcontainer")
        self.app.query_one("#tab_home").terminal_message(f"You leave the town...!")
        minimap_container.remove_children()
        minimap_container.mount(Static("Minimap", classes="generic_tab-title"))
        minimap_container.mount(Static(f"Town: ---", classes="generic_tab-title"))

    @staticmethod
    def enter(app: App, player: PlayerTile, game_map: LocationMap):
        container = app.query_one("#minimapcontainer")
        container.mount(LocationView(player, game_map))

class Town:
    def __init__(self, name, description, buildings, exit, townview: TownView):
        self.name = name
        self.description = description
        self.buildings = buildings  # List of building objects
        self.townview = townview
        self.exit = exit
    
    def get_building_at(self, x, y):
        for building in self.buildings:
            if building.x == x and building.y == y:
                return building
        if x in range(self.exit.start_x, self.exit.end_x) and y in range(self.exit.start_y, self.exit.end_y):
            return self.exit
        return None

class Exit:
    def __init__(self, start_x, start_y, end_x, end_y, tile_char):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.tile_char = tile_char

class Building:
    def __init__(self, name, type, x, y, tile_char, description):
        self.name = name
        self.type = type  # 'inn', 'blacksmith', etc.
        self.x = x
        self.y = y
        self.tile_char = tile_char
        self.description = description

class Inn(Building):
    def __init__(self, name, x, y, tile_char, description, cost_per_night, healing_amount):
        super().__init__(name, 'inn', x, y, tile_char, description)
        self.cost_per_night = cost_per_night
        self.healing_amount = healing_amount
    
    def rest(self, player: cs.Player, locationview):
        # Access the app to show messages in the console
        app = locationview.app
        home_tab = app.query_one("#tab_home")
        character_tab = app.query_one("#tab_character")

        
        if player.currencypoints < self.cost_per_night:
            home_tab.terminal_message("You don't have enough money to rest here! Get some and then come back!")
            return
        
        player.currencypoints -= self.cost_per_night

        cost = cs.Cost.translate_from_currency_ponts(self.cost_per_night)
        coststring = ""
        for key in cost:
            coststring = coststring + f" {cost[key]}{key}"

        cost2 = cs.Cost.translate_from_currency_ponts(player.currencypoints)
        coststring2 = ""
        for key in cost2:
            coststring2 = coststring2 + f" {cost2[key]}{key}"
        if coststring2 == "":
            coststring2 = " No Money!"

        home_tab.terminal_message(f"You pay the Inn Keeper{coststring} to stay the night...")
        home_tab.terminal_message(f"You now have{coststring2}")

        # Heal the player
        player.set_health(min(player.get_health() + self.healing_amount, player.get_max_health()))
        home_tab.health = player.get_health()
        home_tab.max_health = player.get_max_health()
        home_tab.currencypoints = player.get_currencypoints()
        character_tab.health = player.get_health()
        character_tab.max_health = player.get_max_health()
        character_tab.currencypoints = player.get_currencypoints()
        
        # Show message in console
        home_tab.terminal_message(f"You rest at {self.name}. Health restored to {player.get_health()}!")
        app.save_game()


class Blacksmith(Building):
    def __init__(self, name, x, y, tile_char, description, items_for_sale):
        super().__init__(name, 'blacksmith', x, y, tile_char, description)
        self.items_for_sale = items_for_sale
    
    def show_items(self, locationview):
        # Access the app to show messages in the console
        app = locationview.app
        home_tab = app.query_one("#tab_home")
        
        # Show available items
        home_tab.terminal_message(f"{self.name} offers these items:")
        for item in self.items_for_sale:
            home_tab.terminal_message(f"- {item.name} ({item.cost.quantity}{item.cost.unit})")
        
        # Prompt to buy
        home_tab.terminal_message("Type 'buy <item name>' to purchase")

    def buy_item(self, player, item_name, locationview):
        # Access the app to show messages in the console
        app = locationview.app
        home_tab = app.query_one("#tab_home")
        character_tab = app.query_one("#tab_character")

        # Find the item
        item_to_buy = None
        for item in self.items_for_sale:
            if item.name.lower() == item_name.lower():
                item_to_buy = item
                break
        
        if not item_to_buy:
            home_tab.terminal_message(f"Sorry, we don't have '{item_name}'")
            return

        cost = item_to_buy.cost
        currencypointcost = cs.Cost.translate_to_currency_points(cost)
        
        if player.currencypoints < currencypointcost:
            home_tab.terminal_message(f"You don't have enough money to buy a {item_to_buy.name}!")
            return
        
        player.currencypoints -= currencypointcost

        cost2 = cs.Cost.translate_from_currency_ponts(player.currencypoints)
        coststring2 = ""
        for key in cost2:
            coststring2 = coststring2 + f" {cost2[key]}{key}"
        if coststring2 == "":
            coststring2 = " No Money"
        
        player.inventory.append(item_to_buy)
        home_tab.terminal_message(f"You bought a {item_to_buy.name} for {cost.quantity}{cost.unit}!")
        home_tab.terminal_message(f"You now have{coststring2}!")
        home_tab.currencypoints = player.get_currencypoints()
        character_tab.currencypoints = player.get_currencypoints()
        app.save_game()
        app.query_one("#tab_inventory").refresh_content()

class CombatState:
    def __init__(self, player, zombies, home_tab):
        self.player = player
        self.zombies = zombies
        self.home_tab = home_tab
        self.current_turn = "player"
        self.active = True
        self.waiting_for_input = False
        self.current_prompt = ""

def windwood_dungeon(player: cs.Player, home_tab):
    zombiecount = random.randrange(1, 4)
    zombies = [cs.Zombie(max_health=random.randint(8, 12), damage_dice=cs.Dice(1, 6)) 
               for _ in range(zombiecount)]
    
    home_tab.terminal_message("You enter the Windwood Forest dungeon. The ground is slathered in green mold and reeks of death.")
    home_tab.terminal_message(f"You encounter {len(zombies)} zombies!")
    
    # Create and store combat state
    combat = CombatState(player, zombies, home_tab)
    home_tab.app.combat_state = combat
    start_player_turn(combat)

def start_player_turn(combat):
    combat.current_turn = "player"
    combat.waiting_for_input = True
    combat.home_tab.terminal_message("--- YOUR TURN ---")
    combat.home_tab.terminal_message(f"Your health: {cs.player.get_health()}/{cs.player.get_max_health()}")
    
    # List available weapons (both equipped and in inventory)
    weapons = []
    for item in cs.player.equipped_inventory:
        try:
            item.is_weapon()
            weapons.append(item)
        except:
            print("")
    
    combat.home_tab.terminal_message("Available weapons:")
    for i, weapon in enumerate(weapons, 1):
        combat.home_tab.terminal_message(f"{i}. {weapon.name} (Damage: {weapon.damage.damage_dice.retranslate()})")
    
    combat.home_tab.terminal_message("Type 'attack X' to use weapon X or 'flee' to escape")
    combat.current_prompt = "What will you do? "

def process_combat_command(combat, command):
    command = command.lower().strip()
    
    if command.startswith("attack"):
        try:
            # Get weapon number from command
            weapon_num = int(command.split()[1])
            weapons = []
            for item in cs.player.equipped_inventory:
                try:
                    item.is_weapon()
                    weapons.append(item)
                except:
                    print("")
            
            if 1 <= weapon_num <= len(weapons):
                weapon = weapons[weapon_num-1]
                target = random.choice(combat.zombies)
                
                # Roll damage
                damage_rolls = [random.randint(1, int(weapon.damage.damage_dice.dice)) 
                               for _ in range(int(weapon.damage.damage_dice.amount))]
                total_damage = sum(damage_rolls)
                
                # Apply damage
                target.health -= total_damage
                combat.home_tab.terminal_message(f"You hit a zombie with {weapon.name} for {total_damage} damage! ({damage_rolls})")
                
                # Check if zombie died
                if target.health <= 0:
                    combat.home_tab.terminal_message("The zombie dies!")
                    combat.zombies.remove(target)
                
                # Check if combat ended
                if not combat.zombies:
                    end_combat_victory(combat)
                    return
                
                # Zombie turn
                start_zombie_turn(combat)
            else:
                combat.home_tab.terminal_message("Invalid weapon number!")
                combat.waiting_for_input = True
        except (ValueError, IndexError):
            combat.home_tab.terminal_message("Invalid command! Use 'attack X' where X is weapon number")
            combat.waiting_for_input = True
    
    elif command == "flee":
        if random.random() < 0.5:  # 50% chance to escape
            combat.home_tab.terminal_message("You successfully flee from the dungeon!")
            combat.home_tab.app.combat_state = None
        else:
            combat.home_tab.terminal_message("You failed to escape!")
            start_zombie_turn(combat)
    
    else:
        combat.home_tab.terminal_message("Invalid command! Use 'attack X' or 'flee'")
        combat.waiting_for_input = True

def start_zombie_turn(combat):
    combat.current_turn = "zombie"
    combat.waiting_for_input = False
    combat.home_tab.terminal_message("--- ZOMBIES' TURN ---")
    
    for zombie in combat.zombies:
        damage = zombie.attack()
        cs.player.set_health(cs.player.get_health() - damage)
        combat.home_tab.terminal_message(f"A zombie hits you for {damage} damage!")
        
        # Update health displays
        combat.home_tab.health = cs.player.get_health()
        combat.home_tab.app.query_one("#tab_character").health = cs.player.get_health()
        
        if cs.player.get_health() <= 0:
            end_combat_defeat(combat)
            return
    
    # Back to player turn
    start_player_turn(combat)

def end_combat_victory(combat):
    combat.home_tab.terminal_message("You defeated all zombies!")
    
    # Add rewards
    gold = random.randint(5, 20)
    exp = random.randint(10, 30)
    
    cs.player.set_currencypoints(cs.player.get_currencypoints() + cs.Cost.translate_to_currency_points(cs.Cost(gold, "gp")))
    cs.player.level.add_current_exp(exp)
    
    combat.home_tab.terminal_message(f"Found {gold} gold pieces!")
    combat.home_tab.terminal_message(f"Gained {exp} experience points!")

    # Update displays
    combat.home_tab.currencypoints = cs.player.get_currencypoints()
    combat.home_tab.app.query_one("#tab_character").exp = cs.player.level.get_current_exp()
    combat.home_tab.app.query_one("#tab_character").level = cs.player.level.get_level()

    PlayerTile.travel_message(combat.home_tab.app)
    
    combat.home_tab.app.combat_state = None

def end_combat_defeat(combat):
    combat.home_tab.terminal_message("You have been defeated!")
    combat.home_tab.terminal_message("You wake up outside the dungeon with half health...")

    PlayerTile.travel_message(combat.home_tab.app)
    
    # Penalty for defeat
    cs.player.set_health(max(1, cs.player.get_max_health() // 2))
    combat.home_tab.health = cs.player.get_health()
    combat.home_tab.app.query_one("#tab_character").health = cs.player.get_health()
    
    combat.home_tab.app.combat_state = None