from constants import *
from random import choice


class Character:    # TODO: An object used to describe the character with all its attributes and statistics.
    def __init__(self):
        self.race = choice(RACES)
        self.gender = choice(GENDERS)
        self.first_name = choice(DND5E_DICT["Races"][self.race]["First Names"][self.gender])
        self.last_name = choice(DND5E_DICT["Races"][self.race]["Last Names"])
        self.age = ""
        self.height = ""
        self.weight = ""
        self.skin_color = ""
        self.hairskin_color = ""
        self.eyeskin_color = ""
        self.accent = ""
        self.voice_type = ""
        self.background = ""
        self.memorable_trait = ""
        self.languages = ""
        self.deity = ""
        self.alignment = ""
        self.homeland = ""


class Adventurer(Character):
    def __init__(self):
        pass


class Bard(Adventurer):
    def __init__(self):
        pass


class Cleric(Adventurer):
    def __init__(self):
        pass


class Druid(Adventurer):
    def __init__(self):
        pass


class Fighter(Adventurer):
    def __init__(self):
        pass


class Monk(Adventurer):
    def __init__(self):
        pass


class Paladin(Adventurer):
    def __init__(self):
        pass


class Ranger(Adventurer):
    def __init__(self):
        pass


class Rogue(Adventurer):
    def __init__(self):
        pass


class Sorcerer(Adventurer):
    def __init__(self):
        pass


class Warlock(Adventurer):
    def __init__(self):
        pass


class Wizard(Adventurer):
    def __init__(self):
        pass