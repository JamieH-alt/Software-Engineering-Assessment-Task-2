import random
from textual.app import App, ComposeResult, Widget
from textual.widgets import Header, Footer, TabbedContent, Static, TabPane, MarkdownViewer, Collapsible, Button, Input, Label, Log, ListItem, ListView, Select, Rule
from textual.containers import Grid, VerticalScroll, Vertical, Container, Horizontal, Center
from textual.reactive import reactive
from textual.events import Event
from textual.message import Message
import math

# These are core classes that are inherrited
class Stats(): # This is used so I don't have to constantly define stats.
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self._strength = strength
        self._dexterity = dexterity
        self._constitution = constitution
        self._intelligence = intelligence
        self._wisdom = wisdom
        self._charisma = charisma

    def to_dict(self) -> dict:
        diction = {}
        diction["strength"] = self._strength
        diction["dexterity"] = self._dexterity
        diction["constitution"] = self._constitution
        diction["intelligence"] = self._intelligence
        diction["wisdom"] = self._wisdom
        diction["charisma"] = self._charisma
        return diction
    
    def get_strength(self) -> int:
        return self._strength
    
    def set_strength(self, strength: int):
        self._strength = strength

    def get_dexterity(self) -> int:
        return self._dexterity
    
    def set_dexterity(self, dexterity: int):
        self._dexterity = dexterity
    
    def get_constitution(self) -> int:
        return self._constitution
    
    def set_constitution(self, constitution: int):
        self._constitution = constitution

    def get_intelligence(self) -> int:
        return self._intelligence
    
    def set_intelligence(self, intelligence: int):
        self._intelligence = intelligence

    def get_wisdom(self) -> int:
        return self._wisdom
    
    def set_wisdom(self, wisdom: int):
        self._wisdom = wisdom

    def get_charisma(self):
        return self._charisma
    
    def set_charisma(self, charisma: int):
        self._charisma = charisma

class Race(): # This is the base race class.
    def __init__(self, raceid: int, racename: str, raceurl: str, statbonuses: Stats):
        self.raceid = raceid
        self.racename = racename
        self.raceurl = raceurl
        self.statbonuses = statbonuses

    @staticmethod
    def from_id(id: int):
        match id:
            case 0:
                return Human
            case 1:
                return Elf
            case 2:
                return Dwarf
            case 3:
                return Halfling
            case 4:
                return Dragonborn
            case 5:
                return Tiefling
            case 6:
                return HalfOrc
            case 7:
                return HalfElf
    
    @staticmethod
    def from_name(name: str):
        match name:
            case "Human":
                return Human
            case "Elf":
                return Elf
            case "Dwarf":
                return Dwarf
            case "Halfling":
                return Halfling
            case "Dragonborn":
                return Dragonborn
            case "Halfling":
                return Halfling
            case "Half-Orc":
                return HalfOrc
            case "Half-Elf":
                return HalfElf
                 

    # Only provides Gets as there will be no situation where a race's bonuses are changed during gameplay and after initialisation (Their inheritance.)

    def get_id(self) -> int:
        return self.raceid

    def get_name(self) -> str:
        return self.racename
    
    def get_url(self) -> str:
        return self.raceurl
    
    def get_statbonuses(self):
        return self.statbonuses

class CharClass():
    def __init__(self, classid: int, classname: str, classurl: str, statbonuses: Stats):
        self.classid = classid
        self.classname = classname
        self.classurl = classurl
        self.statbonuses = statbonuses

    @staticmethod
    def from_id(id: int):
        match id:
            case 0:
                return Barbarian
            case 1:
                return Bard
            case 2:
                return Cleric
            case 3:
                return Druid
            case 4:
                return Fighter
            case 5:
                return Monk
            case 6:
                return Paladin
            case 7:
                return Ranger
            case 8:
                return Rogue
            case 9:
                return Sorcerer
            case 10:
                return Warlock
            case 11:
                return Wizard
            
    @staticmethod
    def from_name(name: str):
        match name:
            case "Barbarian":
                return Barbarian
            case "Bard":
                return Bard
            case "Cleric":
                return Cleric
            case "Druid":
                return Druid
            case "Fighter":
                return Fighter
            case "Monk":
                return Monk
            case "Paladin":
                return Paladin
            case "Ranger":
                return Ranger
            case "Rogue":
                return Rogue
            case "Sorcerer":
                return Sorcerer
            case "Warlock":
                return Warlock
            case "Wizard":
                return Wizard

    # Only provides Gets as there will be no situation where a race's bonuses are changed during gameplay and after initialisation (Their inheritance.)

    def get_id(self) -> int:
        return self.classid

    def get_name(self) -> str:
        return self.classname
    
    def get_url(self) -> str:
        return self.classurl
    
    def get_statbonuses(self):
        return self.statbonuses

# A The Char Races and Classes Setup!
# Core D&D 5E Character Races
Human = Race(0, "Human", "WIP", Stats(1, 1, 1, 1, 1, 1))
Elf = Race(1, "Elf", "WIP", Stats(0, 2, 0, 0, 0, 0))
Dwarf = Race(2, "Dwarf", "WIP", Stats(0, 0, 2, 0, 0, 0))
Halfling = Race(3, "Halfling", "WIP", Stats(0, 2, 0, 0, 0, 0))
Dragonborn = Race(4, "Dragonborn", "WIP", Stats(2, 0, 0, 0, 0, 1))
Tiefling = Race(5, "Tiefling", "WIP", Stats(0, 0, 0, 1, 0, 2))
HalfOrc = Race(6, "Half-Orc", "WIP", Stats(2, 0, 1, 0, 0, 0))
HalfElf = Race(7, "Half-Elf", "WIP", Stats(1, 0, 1, 0, 0, 2))

Races = [Human, Elf, Dwarf, Halfling, Dragonborn, Tiefling, HalfOrc, HalfElf]

# Core D&D 5E Character Classes
Barbarian = CharClass(0, "Barbarian", "WIP", Stats(2, 0, 1, 0, 0, 0))
Bard = CharClass(1, "Bard", "WIP", Stats(0, 0, 0, 0, 0, 2))
Cleric = CharClass(2, "Cleric", "WIP", Stats(0, 0, 0, 0, 2, 0))
Druid = CharClass(3, "Druid", "WIP", Stats(0, 0, 0, 0, 2, 0))
Fighter = CharClass(4, "Fighter", "WIP", Stats(2, 0, 1, 0, 0, 0))
Monk = CharClass(5, "Monk", "WIP", Stats(0, 2, 1, 0, 0, 0))
Paladin = CharClass(6, "Paladin", "WIP", Stats(2, 0, 1, 0, 0, 1))
Ranger = CharClass(7, "Ranger", "WIP", Stats(0, 2, 0, 0, 1, 0))
Rogue = CharClass(8, "Rogue", "WIP", Stats(0, 2, 0, 0, 0, 0))
Sorcerer = CharClass(9, "Sorcerer", "WIP", Stats(0, 0, 0, 0, 0, 2))
Warlock = CharClass(10, "Warlock", "WIP", Stats(0, 0, 0, 1, 0, 2))
Wizard = CharClass(11, "Wizard", "WIP", Stats(0, 0, 0, 2, 0, 0))

Classes = [Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer]

# Base entity, useable for characters and monsters
class Entity():

    def __init__(self, health: int, max_health: int, stats: Stats):
        self._health = health
        self._stats = stats
        self._max_health = max_health

    def set_health(self, amount: int):
        self._health = amount
    
    def get_health(self) -> int:
        return self._health

    def set_stats(self, stats: Stats):
        self._stats = stats
    
    def get_stats(self) -> Stats:
        return self._stats
    
    def set_max_health(self, amount: int):
        self._max_health = amount

    def get_max_health(self) -> int:
        return self._max_health

# The following are all used for spells
# Effects are what actually enable the spells to do anything and are an "executeable"

class Effect(): # This is just the base effect class
    def __init__(self, type: int, target, amount: int):
        self._type = type
        self._target = target
        self._amount = amount

class DamageEffect(Effect): # This is a basic Damage Effect
    def __init__(self, type: int, target, amount: int):
        super().__init__(type, target, amount)

    @classmethod # This is so that we can cast the Effect() class to the DamageEffect class !!! This is important as otherwise we wouldn't be able to use Effect for an overarching instance with type "inferencing"
    def DamageEffect_from_base(cls, base_instance):
        return cls(base_instance)
    
    def activate_effect(self):
        self._target.set_health -= self._amount

# Pretty much a glorified dictionary (a.k.a a struct) besides the effect system
class Spell():
    def __init__(self, name: str, level: int, school, effect, castingtime: int, duration: int, range: int, components: list, description: str, targetdescription: str, activatordescription: str):
        self._name = reactive(name)
        self._level = level
        self._school = school
        self._effect = effect
        self._castingtime = castingtime
        self._duration = duration
        self._range = range
        self._components = components
        self._description = description
        self._targetdescription = targetdescription
        self._activatordescription = activatordescription

    # These are all protected for the same reason as the CharClass and Race Stats

    def get_name(self) -> str:
        return self._name

    def get_level(self) -> int:
        return self._level

    def get_school(self):
        return self._school

    def get_castingtime(self) -> int:
        return self._castingtime

    def get_duration(self) -> int:
        return self._duration

    def get_range(self) -> int:
        return self._range

    def get_components(self) -> list:
        return self._components

    def get_description(self) -> str:
        return self._description
    
    def get_targetdescription(self) -> str:
        return self._targetdescription
    
    def get_activatordescription(self) -> str:
        return self._activatordescription
    
    def activate_spell(self, target: Entity, activator: Entity) -> str:
        # This gets run every turn that the spell is activated for in the terminal
        if isinstance(self._effect, DamageEffect):
            effect: DamageEffect = DamageEffect.DamageEffect_from_base(self._effect)
            effect.activate_effect()
            if isinstance(target, Character):
                return self._targetdescription
            elif isinstance(activator, Character):
                return self._activatordescription   

# Character Class
# This is able to be used for NPC's if they are added in the future
class Character(Entity):
    def __init__(self, name: str, race: Race, charclass: CharClass, stats: Stats, hitpoints: int, armorclass: int, proficiencybonus: int, spells: list[Spell]):
        super().__init__(15, 15, stats)
        self._name = name
        self._race = race
        self._charclass = charclass
        self.hitpoints = hitpoints
        self.armorclass = armorclass
        self.proficiencybonus = proficiencybonus
        self.spells = spells
        self.currencypoints = 0

    def get_currencypoints(self) -> int:
        return self.currencypoints

    def set_currencypoints(self, amount: int):
        self.currencypoints = amount
    
    def get_race(self) -> Race:
        return self._race
    
    def get_class(self) -> CharClass:
        return self._charclass
    
    def set_hitpoints(self, hitpoints: int):
        self.hitpoints = hitpoints
    
    def get_hitpoints(self) -> int:
        return self.hitpoints
    
    def set_armorclass(self, armorclass: int):
        self.armorclass = armorclass
    
    def get_armorclass(self) -> int:
        return self.armorclass

    def set_proficiencybonus(self, proficiencybonus: int):
        self.proficiencybonus = proficiencybonus
    
    def get_proficiencybonus(self) -> int:
        return self.proficiencybonus
    
    def add_spell(self, spell: Spell) -> list[Spell]:
        self.spells.append(spell)
        return self.spells
    
    def remove_spell(self, spell: Spell) -> list[Spell]:
        self.spells.remove(spell)
        return self.spells
    
    def get_spells(self) -> list[Spell]:
        return self.spells

# These are setup for the following Item Classes, They are basically just structs and hardly count as classes
    
class APIObject():
    def __init__(self, index: str, name: str, url: str):
        self.index = index
        self.name = name
        self.url = url

costcolours = {
    "pp": "#ddfaff",
    "gp": "#ffcb69",
    "ep": "#79d872",
    "sp": "#778490",
    "cp": "#b65d17"
} # This is used for making money pretty !

class Cost():
    def __init__(self, quantity: int, unit: str):
        self.quantity = quantity
        self.unit = unit
    
    @staticmethod
    def translate(amount: str) -> 'Cost':
        if "cp" in amount:
            return Cost(amount.split("c")[0], "cp")
        elif "sp" in amount:
            return Cost(amount.split("s")[0], "sp")
        elif "ep" in amount:
            return Cost(amount.split("e")[0], "ep")
        elif "gp" in amount:
            return Cost(amount.split("g")[0], "gp")
    
    def translate_to_currency_points(self) -> int:
        if self.unit == "cp":
            return self.quantity
        elif self.unit == "sp":
            return self.quantity * 10
        elif self.unit == "ep":
            return self.quantity * 50
        elif self.unit == "gp":
            return self.quantity * 100
    
    @staticmethod
    def translate_from_currency_ponts(amount: int) -> dict:
        currencies = {}

        gp = amount // 100
        amount %= 100
        if gp > 0:
            currencies["gp"] = gp

        ep = amount // 50
        amount %= 50
        if ep > 0:
            currencies["ep"] = ep

        sp = amount // 10
        amount %= 10
        if sp > 0:
            currencies["sp"] = sp

        cp = amount
        if cp > 0:
            currencies["cp"] = cp

        return currencies

    @staticmethod
    def cost_from_currencypoints(amount: int, currency: str):
        if currency == "cp":
            return amount
        elif currency == "sp":
            return amount / 10
        elif currency == "ep":
            return amount / 50
        elif currency == "gp":
            return amount / 100

class Dice():
    def __init__(self, amount: int, dice: int):
        self.amount = amount
        self.dice = dice
    
    def translate(string):
        x = string.split("d")
        return Dice(x[0], x[1])
    
    def retranslate(self):
        return f"{self.amount}d{self.dice}"

    def roll(self):
        y = []
        for i in range(0, self.amount):
            y.append(random.randrange(0, self.dice))

class Damage():
    def __init__(self, damage_dice: Dice, damage_type: APIObject):
        self.damage_dice = damage_dice
        self.damage_type = damage_type

class EquipButton(Button):
    def __init__(self, label, variant, id, player_ref: 'Player', item_ref: 'Item'):
        super().__init__(label=label, variant=variant, id=id)
        self.player_ref = player_ref
        self.item_ref = item_ref

    
    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == self.id:
            if self.item_ref in self.player_ref.equipped_inventory:
                event.button.variant="success"
                event.button.label="Equip"
                self.player_ref.unequip_item(self.item_ref)
            else:
                event.button.variant="error"
                event.button.label="Unequip"
                self.player_ref.equip_item(self.item_ref)
        app = self.app
        home_tab = app.query_one("#tab_home")
        inventory_tab = app.query_one("#tab_inventory")
        home_tab.refresh_content()
        inventory_tab.refresh_content()
        app.save_game()

item_collapsed_states = {} # This is important for when items are reloaded

# This item class provides the widget, and other variables for weapons and armour.
class Item():
    def __init__(self, desc: list, special: list, index: str, name: str, equipment_category: APIObject, gear_category: APIObject, cost: Cost, weight: int, url: str, contents: list, properties: list):
        self.desc = desc
        self.special = special
        self.index = index
        self.name = name
        self.equipment_category = equipment_category
        self.gear_category = gear_category
        self.cost = cost
        self.weight = weight
        self.url = url
        self.contents = contents
        self.properties = properties

    def get_widget(self, player: 'Player'):
        collapsed = item_collapsed_states.get(self.index, True)

        widget = Collapsible(
            VerticalScroll(
                Static(self.equipment_category.name),
                Rule(),
                Horizontal(
                    Vertical(
                        Static(self.gear_category.name) if self.gear_category.name != "unknown" else Rule(),
                        Static(f"Costs: {self.cost.quantity}{self.cost.unit}"),
                        Static(f"Weight: {self.weight}lbs"),
                        classes="item-verticalscroll"
                    ),
                    classes="item-verticalscroll"
                ),
                classes="item-verticalscroll"
            ),
        title=self.name, collapsed=collapsed)

        widget.item_ref = self

        return widget

    @staticmethod
    def on_collapsible_toggled(event: Collapsible.Collapsed):
        if hasattr(event.collapsible, 'item_ref'):
            item_collapsed_states[event.collapsible.item_ref.index] = event.collapsible

class Weapon(Item):
    def __init__(self, desc: list, special: list, index: str, name: str, equipment_category: APIObject, gear_category: APIObject, cost: Cost, weight: int, url: str, contents: list, properties: list, weapon_category: str, weapon_range: str, category_range: str, damage: Damage, range: dict):
        super().__init__(desc, special, index, name, equipment_category, gear_category, cost, weight, url, contents, properties)
        self.weapon_category = weapon_category
        self.weapon_range = weapon_range
        self.category_range = category_range
        self.damage = damage
        self.range = range

    def get_widget(self, player: 'Player'):
        equipped = self in player.equipped_inventory
        label = "Unequip" if equipped else "Equip"
        button_id = f"equip_{self.index}"

        collapsed = item_collapsed_states.get(self.index, True)

        widget = Collapsible(
            VerticalScroll(
                Static(self.equipment_category.name),
                Static(self.weapon_category),
                Rule(),
                Horizontal(
                    Vertical(
                        Static(f"Damage: {self.damage.damage_dice.retranslate()}"),
                        Static(f"Damage Type: {self.damage.damage_type.name}"),
                        Static(f"Costs: {self.cost.quantity}{self.cost.unit}"),
                        Static(f"Weight: {self.weight}lbs"), 
                        classes="item-verticalscroll"
                        ),
                    Vertical(
                        EquipButton(label, variant="error" if equipped else "success", id=f"{button_id}", player_ref=player, item_ref=self),
                        classes="item-verticalscroll"
                    ),
                    classes="item-verticalscroll"
                ),
                classes="item-verticalscroll"
            ),
        title=self.name, collapsed=collapsed)   

        widget.item_ref = self

        return widget
    
    @staticmethod
    def on_collapsible_toggled(event: Collapsible.Collapsed):
        if hasattr(event.collapsible, 'item_ref'):
            item_collapsed_states[event.collapsible.item_ref.index] = event.collapsible

    def is_weapon(self):
        return True

class ArmourClass():
    def __init__(self, base: int, dex_bonus: bool, max_bonus: int):
        self.base = base
        self.dex_bonus = dex_bonus
        self.max_bonus = max_bonus

class Armour(Item):
    def __init__(self, desc: list, special: list, index: str, name: str, equipment_category: APIObject, gear_category: APIObject, cost: Cost, weight: int, url: str, contents: list, properties: list, armor_category: str, armor_class: ArmourClass, str_minimum: int, stealth_disadvantage: bool):
        super().__init__(desc, special, index, name, equipment_category, gear_category, cost, weight, url, contents, properties)
        self.armor_category = armor_category
        self.armor_class = armor_class
        self.str_minimum = str_minimum
        self.stealth_disadvantage = stealth_disadvantage
    
    def get_widget(self, player: 'Player'):
        equipped = self in player.equipped_inventory
        label = "Unequip" if equipped else "Equip"
        button_id = f"equip_{self.index}"

        collapsed = item_collapsed_states.get(self.index, True)

        widget = Collapsible(
            VerticalScroll(
                Static(self.equipment_category.name),
                Static(f"{self.armor_category} Armour"),
                Rule(),
                Horizontal(
                    Vertical(
                        Static(f"Armour Class: {self.armor_class.base}"),
                        Static(f"Strength Minimum: {self.str_minimum}"),
                        Static(f"Stealth Disadvantage: {self.stealth_disadvantage}"),
                        Static(f"Costs: {self.cost.quantity}{self.cost.unit}"),
                        Static(f"Weight: {self.weight}lbs"),
                        classes="item-verticalscroll"
                    ),
                    Vertical(
                        EquipButton(label, variant="error" if equipped else "success", id=f"{button_id}", player_ref=player, item_ref=self),
                        classes="item-verticalscroll"
                    ),
                    classes="item-verticalscroll"
                    ),
                classes="item-verticalscroll"
            ),
        title=self.name, collapsed=collapsed)

        widget.item_ref = self

        return widget

# Levels
"""
Levels are pretty self explanatary,
They basically just provide a way to upgrade the player a little,
There will be more math later on in the program's stages, mainly adding an ability to level up the characters stats.
"""
class Level():
    def __init__(self, level: int):
        self.level = level
        self.currentexp = 0
        self.required_exp_amt = self.required_exp(self.level + 1)

    def get_level(self) -> int:
        return self.level
    
    def get_current_exp(self) -> int:
        return self.currentexp

    def add_current_exp(self, add: int) -> None:
        self.currentexp += add
    
    def level_up(self) -> None:
        self.level += 1
        self.currentexp = 0
        self.required_exp_amt = self.required_exp(self.level + 1)
        # Character Stat Leveling Here
    
    @staticmethod
    def required_exp(level: int) -> int:
        return int(20 * level ** 1.35 + 30 * level)
    
# This player class inherits from character for future proofing in the case of NPC's etc.
# It comes after the Item Classes so It can reference them as python doesn't allow for non-chronological usage of classes / functions in references
class Player(Character):
    def __init__(self, name: str, race: Race, charclass: CharClass, stats: Stats, hitpoints: int, armorclass: int, proficiencybonus: int, spells: list[Spell], inventory: list[Item, Armour, Weapon], equipped_inventory = list[Armour, Weapon]):
        super().__init__(name, race, charclass, stats, hitpoints, armorclass, proficiencybonus, spells)
        self.inventory = inventory
        self.equipped_inventory = equipped_inventory
        self.level = Level(1)
        self.in_location = False
        self.x = 0
        self.y = 0
        self.travel_multiplier = 1
        self.playertile = None

    def equip_item(self, item):
        # Add Stats here !!!
        if item not in self.equipped_inventory:
            self.equipped_inventory.append(item)

    def unequip_item(self, item):
        if item in self.equipped_inventory:
            self.equipped_inventory.remove(item)

    def serialize(self) -> dict:
        return {
            "name": self._name,
            "race_id": self._race.raceid,
            "class_id": self._charclass.classid,
            "stats": self._stats.to_dict(),
            "hitpoints": self.hitpoints,
            "armorclass": self.armorclass,
            "proficiencybonus": self.proficiencybonus,
            "inventory": [item.index for item in self.inventory],
            "equipped_inventory": [item.index for item in self.equipped_inventory],
            "level": self.level.level,
            "currentexp": self.level.currentexp,
            "currencypoints": self.currencypoints,
            "spells": self.spells,
            "health": self._health,
            "max_health": self._max_health
        }
    
player = Player(
    "Bobathy",
    Human,
    Barbarian,
    Stats(0, 0, 0, 0, 0, 0),
    15,
    5,
    5,
    [],
    [],
    []
)

# This is just a hodgepodge quick and easy zombie. If I had more time this would be implemented with the Entity system.
class Zombie():
    def __init__(self, max_health: int, damage_dice: Dice):
        self.max_health = max_health
        self.health = max_health
        self.damage_dice = damage_dice
    
    def attack(self) -> int:
        total = 0
        for _ in range(int(self.damage_dice.amount)):
            total += random.randint(1, self.damage_dice.dice)
        return total