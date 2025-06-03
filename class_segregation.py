import random
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, TabbedContent, Static, TabPane, MarkdownViewer, Collapsible, Button, Input, Label, Log, ListItem, ListView, Select, Rule
from textual.containers import Grid, VerticalScroll, Vertical, Container, Horizontal, Center
from textual.reactive import reactive
from textual.events import Event

# These are core classes that are inherrited
class Stats(): # This is used so I don't have to constantly define stats.
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self._strength = strength
        self._dexterity = dexterity
        self._constitution = constitution
        self._intelligence = intelligence
        self._wisdom = wisdom
        self._charisma = charisma
    
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

    # Only provides Gets as there will be no situation where a race's bonuses are changed during gameplay and after initialisation (Their inheritance.)

    def get_id(self) -> int:
        return self.raceid

    def get_name(self) -> str:
        return self.racename
    
    def get_url(self) -> str:
        return self.raceurl
    
    def get_statbonuses(self):
        return self.statbonuses
    
# This is a race type,


"""
I Don't Combine Races and Character classes into a more generalised class as I would like to be able to
add differences to them individually and tweak the ids. It also allows me to check their url against difference links.
"""

class CharClass():
    def __init__(self, classid: int, classname: str, classurl: str, statbonuses: Stats):
        self.classid = classid
        self.classname = classname
        self.classurl = classurl
        self.statbonuses = statbonuses

    # Only provides Gets as there will be no situation where a race's bonuses are changed during gameplay and after initialisation (Their inheritance.)

    def get_id(self) -> int:
        return self.classid

    def get_name(self) -> str:
        return self.classname
    
    def get_url(self) -> str:
        return self.classurl
    
    def get_statbonuses(self):
        return self.statbonuses

class Entity():
    def __init__(self, health: int, stats: Stats):
        self._health = health
        self._stats = stats
    
    def set_health(self, amount: int):
        self._health = amount
    
    def get_health(self) -> int:
        return self._health

    def set_stats(self, stats: Stats):
        self._stats = stats
    
    def get_stats(self) -> Stats:
        return self._stats

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

class Spell():
    def __init__(self, name: str, level: int, school, effect, castingtime: int, duration: int, range: int, components: list, description: str, targetdescription: str, activatordescription: str):
        self._name = name
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
class Character(Entity):
    def __init__(self, name: str, race: Race, charclass: CharClass, stats: Stats, hitpoints: int, armorclass: int, proficiencybonus: int, spells: list[Spell]):
        super().__init__(100, stats)
        self._name = name
        self._race = race
        self._charclass = charclass
        self.hitpoints = hitpoints
        self.armorclass = armorclass
        self.proficiencybonus = proficiencybonus
        self.spells = spells
    
    def get_race(self) -> Race:
        return self._race
    
    def get_class(self) -> CharClass:
        return self._charclass
    
    def set_hitpoints(self, hitpoints: int):
        self._hitpoints = hitpoints
    
    def get_hitpoints(self) -> int:
        return self._hitpoints
    
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
    
class APIObject():
    def __init__(self, index: str, name: str, url: str):
        self.index = index
        self.name = name
        self.url = url

class Cost():
    def __init__(self, quantity: int, unit: str):
        self.quantity = quantity
        self.unit = unit

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

    def get_widget(self):
        return Collapsible(
            VerticalScroll(
                Static(self.equipment_category.name),
                Rule(),
                Horizontal(
                    Vertical(
                        Static(self.gear_category.name) if self.gear_category.name != "unknown" else Rule(),
                        Static(f"Costs: {self.cost.quantity}{self.cost.unit}"),
                        Static(f"Weight: {self.weight}"),
                        classes="item-verticalscroll"
                    ),
                    Vertical(
                        Button("Equip"),
                        classes="item-verticalscroll"
                    ),
                    classes="item-verticalscroll"
                ),
                classes="item-verticalscroll"
            ),
        title=self.name, collapsed=True)


class Weapon(Item):
    def __init__(self, desc: list, special: list, index: str, name: str, equipment_category: APIObject, gear_category: APIObject, cost: Cost, weight: int, url: str, contents: list, properties: list, weapon_category: str, weapon_range: str, category_range: str, damage: Damage, range: dict):
        super().__init__(desc, special, index, name, equipment_category, gear_category, cost, weight, url, contents, properties)
        self.weapon_category = weapon_category
        self.weapon_range = weapon_range
        self.category_range = category_range
        self.damage = damage
        self.range = range

    def get_widget(self):
        return Collapsible(
            VerticalScroll(
                Static(self.equipment_category.name),
                Static(self.weapon_category),
                Rule(),
                Horizontal(
                    Vertical(
                        Static(f"Damage: {self.damage.damage_dice.retranslate()}"),
                        Static(f"Damage Type: {self.damage.damage_type.name}"),
                        Static(f"Costs: {self.cost.quantity}{self.cost.unit}"),
                        Static(f"Weight: {self.weight}"), classes="item-verticalscroll"
                        ),
                    Vertical(
                        Button("Equip"),
                        classes="item-verticalscroll"
                    ),
                    classes="item-verticalscroll"
                ),
                classes="item-verticalscroll"
            ),
        title=self.name, collapsed=True)   

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
    
    def get_widget(self):
        return Collapsible(
            VerticalScroll(
                Static(self.equipment_category.name)
            ),
        title=self.name, collapsed=True)
