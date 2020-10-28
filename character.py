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
        self.speed = DND5E_DICT["Races"][self.race]["Traits"]["Speed"]
        self.racial_ability_score_bonus = get_racial_ability_score_bonus(self.race, self.subrace)
        self.racial_bonuses = get_racial_bonuses(self.race, self.subrace, self.skin_color)


class Adventurer(Character):
    def __init__(self):
        super().__init__()
        self.dnd_class = choice(CLASSES)
        self.level = randrange(1, 21)
        self.archetype = choice(list(DND5E_DICT["Classes"][self.dnd_class]["Archetypes"].keys()))
        self.class_features = {}
        self.ability_score_pool = 0
        self.add_class_features()
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.roll_ability_scores()
        self.add_ability_score_bonuses()
        self.inspiration = choice([0, 1])
        self.hit_die = int(DND5E_DICT["Classes"][self.dnd_class]["Hit Die"][1:])
        self.max_hit_points = self.roll_hit_points()
        self.proficiency_bonus = int(DND5E_DICT["Classes"][self.dnd_class]["Resources"][f"Level {self.level}"]
                                     ["Proficiency Bonus"][1:])
        # if self.dnd_class in SPELL_CASTING_CLASSES:
        #     self.known

    @property
    def strength_modifier(self):
        return (self.strength - 10) // 2

    @property
    def constitution_modifier(self):
        return (self.constitution - 10) // 2

    @property
    def dexterity_modifier(self):
        return (self.dexterity - 10) // 2

    @property
    def intelligence_modifier(self):
        return (self.intelligence - 10) // 2

    @property
    def wisdom_modifier(self):
        return (self.wisdom - 10) // 2

    @property
    def charisma_modifier(self):
        return (self.charisma - 10) // 2

    def add_class_features(self):
        for level in DND5E_DICT["Classes"][self.dnd_class]["Features"]:
            if int(level[6:]) <= self.level:
                class_feature_items = DND5E_DICT["Classes"][self.dnd_class]["Features"][level].items()
                for feature, description in class_feature_items:
                    if feature != "Ability Score Improvement":
                        self.class_features.update({feature: description})
                    else:
                        self.ability_score_pool += 2
        for level in DND5E_DICT["Classes"][self.dnd_class]["Archetypes"][self.archetype]:
            if int(level[6:]) <= self.level:
                archetype_feature_items = DND5E_DICT["Classes"][self.dnd_class]["Archetypes"][self.archetype][level].items()
                self.class_features.update({feature: description for feature, description in archetype_feature_items if feature != "Ability Score Improvement"})

    def roll_ability_scores(self):
        ability_scores = [
            sum(roll_dice(4, 6)[1:]),
            sum(roll_dice(4, 6)[1:]),
            sum(roll_dice(4, 6)[1:]),
            sum(roll_dice(4, 6)[1:]),
            sum(roll_dice(4, 6)[1:]),
            sum(roll_dice(4, 6)[1:]),
        ]
        self.distribute_ability_scores(ability_scores)

    def distribute_ability_scores(self, ability_scores):
        for pos, ability in enumerate(CLASS_ABILITY_SCORE_PRIORITY[self.dnd_class]):
            if ability == "Str":
                self.strength = ability_scores[pos]
            elif ability == "Con":
                self.constitution = ability_scores[pos]
            elif ability == "Dex":
                self.dexterity = ability_scores[pos]
            elif ability == "Int":
                self.intelligence = ability_scores[pos]
            elif ability == "Wis":
                self.wisdom = ability_scores[pos]
            elif ability == "Cha":
                self.charisma = ability_scores[pos]

    def add_ability_score_bonuses(self):
        self.add_racial_ability_score_bonuses()
        self.spend_ability_score_pool()

    def add_racial_ability_score_bonuses(self):
        for ability in self.racial_ability_score_bonus:
            if ability == "Strength":
                self.strength += self.racial_ability_score_bonus[ability]
            elif ability == "Constitution":
                self.constitution += self.racial_ability_score_bonus[ability]
            elif ability == "Dexterity":
                self.dexterity += self.racial_ability_score_bonus[ability]
            elif ability == "Intelligence":
                self.intelligence += self.racial_ability_score_bonus[ability]
            elif ability == "Wisdom":
                self.wisdom += self.racial_ability_score_bonus[ability]
            elif ability == "Charisma":
                self.charisma += self.racial_ability_score_bonus[ability]
            elif ability == "Any":
                self.ability_score_pool += self.racial_ability_score_bonus["Any"]

    def spend_ability_score_pool(self):
        ability_scores = [
            self.strength,
            self.constitution,
            self.dexterity,
            self.intelligence,
            self.wisdom,
            self.charisma
        ]
        ability_scores.sort(reverse=True)
        for pos, score in enumerate(ability_scores):
            while ability_scores[pos] < 20 and self.ability_score_pool > 0:
                ability_scores[pos] += 1
                self.ability_score_pool -= 1
        self.distribute_ability_scores(ability_scores)

    def roll_hit_points(self):
        return self.hit_die + sum(roll_dice(self.level-1, self.hit_die)) + self.level * self.constitution_modifier


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


def roll_dice(amount, sides):
    dice_result = []
    for _ in range(amount):
        dice_result.append(randrange(1, (sides+1)))
    dice_result.sort()
    return dice_result


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


def get_racial_ability_score_bonus(race, subrace):
    ability_score_increase_dict = {}
    for ability in DND5E_DICT["Races"][race]["Traits"]["Ability Score Increase"]:
        ability_score_increase_dict.update({ability: DND5E_DICT["Races"][race]["Traits"]["Ability Score Increase"][ability]})
    if subrace != "":
        for ability in DND5E_DICT["Races"][race]["Subraces"][subrace]["Ability Score Increase"]:
            ability_score_increase_dict.update({ability: DND5E_DICT["Races"][race]["Subraces"][subrace]
            ["Ability Score Increase"][ability]})
    return ability_score_increase_dict


def get_racial_bonuses(race, subrace, skin_color):
    racial_bonuses_dict = {}
    for trait in DND5E_DICT["Races"][race]["Traits"]:
        if trait not in ["Age", "Alignment", "Draconic Ancestry", "Languages", "Size", "Weight",
                         "Ability Score Increase", "Speed"]:
            racial_bonuses_dict.update({trait: DND5E_DICT["Races"][race]["Traits"][trait]})
    if subrace != "":
        for trait in DND5E_DICT["Races"][race]["Subraces"][subrace]:
            if trait != "Ability Score Increase":
                racial_bonuses_dict.update({trait: DND5E_DICT["Races"][race]["Subraces"][subrace][trait]})
    if race == "Dragonborn":
        racial_bonuses_dict.update({"Draconic Ancestry": {}})
        for key, value in DND5E_DICT["Races"][race]["Traits"]["Draconic Ancestry"].items():
            if key != "Type":
                racial_bonuses_dict["Draconic Ancestry"].update({key: value})
        racial_bonuses_dict["Draconic Ancestry"].update({"Breath Weapon Details": DND5E_DICT["Races"][race]["Traits"]
        ["Draconic Ancestry"]["Type"][skin_color]})
    return racial_bonuses_dict
