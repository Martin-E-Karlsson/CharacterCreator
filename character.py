from constants import *
from random import choice, randrange


class Character:
    def __init__(self):
        self.race = choice(RACES)
        if "Subraces" in list(DND5E_DICT["Races"][self.race].keys()):
            self.subrace = choice(list(DND5E_DICT["Races"][self.race]["Subraces"].keys()))
        else:
            self.subrace = ""
        self.gender = choice(GENDERS)
        self.first_name = choice(DND5E_DICT["Races"][self.race]["First Names"][self.gender])
        self.last_name = choice(DND5E_DICT["Races"][self.race]["Last Names"])
        self.age = randrange(DND5E_DICT["Races"][self.race]["Traits"]["Age"]["Low"],
                             DND5E_DICT["Races"][self.race]["Traits"]["Age"]["High"])
        self.size = DND5E_DICT["Races"][self.race]["Traits"]["Size"]["Category"]
        self.height = str(randrange(DND5E_DICT["Races"][self.race]["Traits"]["Size"]["Height (cm)"]["Low"],
                                    DND5E_DICT["Races"][self.race]["Traits"]["Size"]["Height (cm)"]["High"])) + " cm"
        self.weight = str(randrange(DND5E_DICT["Races"][self.race]["Traits"]["Size"]["Weight (kg)"]["Low"],
                                    DND5E_DICT["Races"][self.race]["Traits"]["Size"]["Weight (kg)"]["High"])) + " kg"
        self.skin_color = get_skin_color(self.race, self.subrace)
        self.hair_color = get_hair_color(self.race, self.subrace)
        if self.race == "Dragonborn":
            self.eye_color = self.skin_color
        else:
            self.eye_color = get_hair_color(self.race, self.subrace)
        self.accent = choice(ACCENTS)
        self.voice_type = choice(VOICE_TYPES)
        self.background = choice(BACKGROUNDS)
        self.memorable_trait = choice(MEMORABLE_TRAITS)
        self.languages = DND5E_DICT["Races"][self.race]["Traits"]["Languages"]
        self.alignment = choice(ALIGNMENTS)
        self.deity = get_deity(self.alignment)


class Adventurer(Character):
    def __init__(self):
        super().__init__()


class Bard(Adventurer):
    def __init__(self):
        super().__init__()


class Cleric(Adventurer):
    def __init__(self):
        super().__init__()


class Druid(Adventurer):
    def __init__(self):
        super().__init__()


class Fighter(Adventurer):
    def __init__(self):
        super().__init__()


class Monk(Adventurer):
    def __init__(self):
        super().__init__()


class Paladin(Adventurer):
    def __init__(self):
        super().__init__()


class Ranger(Adventurer):
    def __init__(self):
        super().__init__()


class Rogue(Adventurer):
    def __init__(self):
        super().__init__()


class Sorcerer(Adventurer):
    def __init__(self):
        super().__init__()


class Warlock(Adventurer):
    def __init__(self):
        super().__init__()


class Wizard(Adventurer):
    def __init__(self):
        super().__init__()


def get_skin_color(race, subrace):
    if race in ["Dwarf", "Halfling", "Human", "Half-Elf"] or subrace in ["Forest Gnome", "Rock Gnome"]:
        return choice(BASIC_SKIN_COLORS)
    elif race == "Dragonborn":
        return choice(list(DND5E_DICT["Races"]["Dragonborn"]["Traits"]["Draconic Ancestry"]["Type"].keys()))
    elif race == ["Half-Orc"]:
        return choice(HALF_ORC_SKIN_COLORS)
    elif race == "Tiefling":
        return choice(TIEFLING_SKIN_COLORS)
    elif subrace in ["Hill Dwarf"]:
        return choice(BASIC_SKIN_COLORS)
    elif subrace in ["Mountain Dwarf"]:
        return choice(LIGHT_BASIC_SKIN_COLORS)
    elif subrace == "High Elf":
        return choice(HIGH_ELF_SKIN_COLORS)
    elif subrace == "Wood Elf":
        return "Copper"
    elif subrace == "Dark Elf":
        return "Obsidian"
    elif subrace == "Deep Gnome":
        return choice(DEEP_GNOME_SKIN_COLORS)


def get_hair_color(race, subrace):
    if race in ["Dwarf", "Halfling", "Human", "Gnome", "Half-Elf"] or subrace in ["Wood Elf"]:
        return choice(BASIC_HAIR_COLORS)
    elif race == ["Half-Orc"]:
        return "Black"
    elif race == ["Tiefling"]:
        return choice(TIEFLING_HAIR_COLORS)
    elif subrace == "High Elf":
        return choice(HIGH_ELF_HAIR_COLORS)
    elif subrace == "Dark Elf":
        return choice(DARK_ELF_HAIR_COLORS)
    elif subrace == "Deep Gnome":
        return "Gray"
    else:
        return "Hairless"


def get_eye_color(race, subrace):
    if race in ["Dwarf", "Halfling", "Human", "Gnome", "Half-Orc"] or subrace in ["Wood Elf"]:
        return choice(BASIC_EYE_COLORS)
    elif race == "Tiefling":
        return choice(TIEFLING_EYE_COLORS)
    elif subrace == "High Elf" or race == "Half-Elf":
        return choice(BASIC_EYE_COLORS + EXOTIC_EYE_COLORS)
    elif subrace == "Dark Elf":
        return choice(DARK_ELF_EYE_COLORS)
    elif subrace == "Deep Gnome":
        return "Dark Gray"


def get_deity(alignment):
    if alignment == "Lawful Good":
        return choice(LAWFUL_GOOD_DEITIES)
    elif alignment == "Neutral Good":
        return choice(NEUTRAL_GOOD_DEITIES)
    elif alignment == "Chaotic Good":
        return choice(CHAOTIC_GOOD_DEITIES)
    elif alignment == "Lawful Neutral":
        return choice(LAWFUL_NEUTRAL_DEITIES)
    elif alignment == "True Neutral":
        return choice(TRUE_NEUTRAL_DEITIES)
    elif alignment == "Chaotic Neutral":
        return choice(CHAOTIC_NEUTRAL_DEITIES)
    elif alignment == "Lawful Evil":
        return choice(LAWFUL_EVIL_DEITIES)
    elif alignment == "Neutral Evil":
        return choice(NEUTRAL_EVIL_DEITIES)
    elif alignment == "Chaotic Evil":
        return choice(CHAOTIC_EVIL_DEITIES)
