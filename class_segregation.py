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
    def __init__(self, type: int, target: Entity, amount: int):
        self._type = type
        self._target = target
        self._amount = amount

class DamageEffect(Effect): # This is a basic Damage Effect
    def __init__(self, type: int, target: Entity, amount: int):
        super().__init__(type, target, amount)

    @classmethod # This is so that we can cast the Effect() class to the DamageEffect class !!! This is important as otherwise we wouldn't be able to use Effect for an overarching instance with type "inferencing"
    def DamageEffect_from_base(cls, base_instance):
        return cls(base_instance)
    
    def activate_effect(self):
        self._target.set_health -= self._amount

class Spell():
    def __init__(self, name: str, level: int, school, effect: Effect, castingtime: int, duration: int, range: int, components: list, description: str, targetdescription: str, activatordescription: str):
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