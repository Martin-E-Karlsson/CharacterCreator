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
            self.eye_color = get_eye_color(self.race, self.subrace)
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
        self.dnd_class = self.get_class()
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
        self.armor_proficiencies = DND5E_DICT["Classes"][self.dnd_class]["Proficiencies"]["Armor"]
        self.weapon_proficiencies = DND5E_DICT["Classes"][self.dnd_class]["Proficiencies"]["Weapons"]
        self.tool_proficiencies = DND5E_DICT["Classes"][self.dnd_class]["Proficiencies"]["Tools"]
        self.skill_proficiencies = DND5E_DICT["Classes"][self.dnd_class]["Proficiencies"]["Skills"]
        self.saves = DND5E_DICT["Classes"][self.dnd_class]["Saves"]

    @property
    def proficiency_bonus(self):
        return int(DND5E_DICT["Classes"][self.dnd_class]["Resources"][f"Level {self.level}"]["Proficiency Bonus"][1:])

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

    @property
    def strength_save_bonus(self):
        if "Strength" in self.saves:
            return self.proficiency_bonus + self.strength_modifier
        else:
            return self.strength_modifier

    @property
    def athletics_bonus(self):
        if "Athletics" in self.skill_proficiencies:
            return self.proficiency_bonus + self.strength_modifier
        else:
            return self.strength_modifier

    @property
    def constitution_save_bonus(self):
        if "Strength" in self.saves:
            return self.proficiency_bonus + self.constitution_modifier
        else:
            return self.constitution_modifier

    @property
    def dexterity_save_bonus(self):
        if "Dexterity" in self.saves:
            return self.proficiency_bonus + self.dexterity_modifier
        else:
            return self.dexterity_modifier

    @property
    def acrobatics_bonus(self):
        if "Acrobatics" in self.skill_proficiencies:
            return self.proficiency_bonus + self.dexterity_modifier
        else:
            return self.dexterity_modifier

    @property
    def sleight_of_hand_bonus(self):
        if "Sleight of Hand" in self.skill_proficiencies:
            return self.proficiency_bonus + self.dexterity_modifier
        else:
            return self.dexterity_modifier

    @property
    def stealth_bonus(self):
        if "Stealth" in self.skill_proficiencies:
            return self.proficiency_bonus + self.dexterity_modifier
        else:
            return self.dexterity_modifier

    @property
    def intelligence_save_bonus(self):
        if "Intelligence" in self.saves:
            return self.proficiency_bonus + self.intelligence_modifier
        else:
            return self.intelligence_modifier

    @property
    def arcana_bonus(self):
        if "Arcana" in self.skill_proficiencies:
            return self.proficiency_bonus + self.intelligence_modifier
        else:
            return self.intelligence_modifier

    @property
    def history_bonus(self):
        if "History" in self.skill_proficiencies:
            return self.proficiency_bonus + self.intelligence_modifier
        else:
            return self.intelligence_modifier

    @property
    def investigation_bonus(self):
        if "Investigation" in self.skill_proficiencies:
            return self.proficiency_bonus + self.intelligence_modifier
        else:
            return self.intelligence_modifier

    @property
    def nature_bonus(self):
        if "Nature" in self.skill_proficiencies:
            return self.proficiency_bonus + self.intelligence_modifier
        else:
            return self.intelligence_modifier

    @property
    def religion_bonus(self):
        if "Arcana" in self.skill_proficiencies:
            return self.proficiency_bonus + self.intelligence_modifier
        else:
            return self.intelligence_modifier

    @property
    def wisdom_save_bonus(self):
        if "Wisdom" in self.saves:
            return self.proficiency_bonus + self.wisdom_modifier
        else:
            return self.wisdom_modifier

    @property
    def animal_handling_bonus(self):
        if "Animal Handling" in self.skill_proficiencies:
            return self.proficiency_bonus + self.wisdom_modifier
        else:
            return self.wisdom_modifier

    @property
    def insight_bonus(self):
        if "Insight" in self.skill_proficiencies:
            return self.proficiency_bonus + self.wisdom_modifier
        else:
            return self.wisdom_modifier

    @property
    def medicine_bonus(self):
        if "Medicine" in self.skill_proficiencies:
            return self.proficiency_bonus + self.wisdom_modifier
        else:
            return self.wisdom_modifier

    @property
    def perception_bonus(self):
        if "Perception" in self.skill_proficiencies:
            return self.proficiency_bonus + self.wisdom_modifier
        else:
            return self.wisdom_modifier

    @property
    def survival_bonus(self):
        if "Survival" in self.skill_proficiencies:
            return self.proficiency_bonus + self.wisdom_modifier
        else:
            return self.wisdom_modifier

    @property
    def charisma_save_bonus(self):
        if "Charisma" in self.saves:
            return self.proficiency_bonus + self.charisma_modifier
        else:
            return self.charisma_modifier

    @property
    def deception_bonus(self):
        if "Deception" in self.skill_proficiencies:
            return self.proficiency_bonus + self.charisma_modifier
        else:
            return self.charisma_modifier

    @property
    def intimidation_bonus(self):
        if "Intimidation" in self.skill_proficiencies:
            return self.proficiency_bonus + self.charisma_modifier
        else:
            return self.charisma_modifier

    @property
    def performance_bonus(self):
        if "Performance" in self.skill_proficiencies:
            return self.proficiency_bonus + self.charisma_modifier
        else:
            return self.charisma_modifier

    @property
    def persuasion_bonus(self):
        if "Persuasion" in self.skill_proficiencies:
            return self.proficiency_bonus + self.charisma_modifier
        else:
            return self.charisma_modifier

    @property
    def initiative_bonus(self):
        return self.dexterity_modifier

    @property
    def passive_perception(self):
        return 10 + self.perception_bonus

    def get_class(self):
        if self.__class__.__name__ in ["Adventurer"]:
            return choice(CLASSES)
        elif self.__class__.__name__ in ["SpellCaster"]:
            return choice(SPELL_CASTING_CLASSES)
        else:
            return self.__class__.__name__

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


class SpellCaster(Adventurer):
    def __init__(self):
        super().__init__()
        self.known_spells = self.choose_spells()

    @property
    def spell_slots(self):
        return DND5E_DICT["Classes"][self.dnd_class]["Resources"][f"Level {self.level}"]["Spell Slots"]

    @property
    def number_of_cantrips_known(self):
        if self.get_class() in CLASSES_WITH_CANTRIPS:
            return DND5E_DICT["Classes"][self.dnd_class]["Resources"][f"Level {self.level}"]["Cantrips Known"]
        else:
            return 0

    @property
    def number_of_spells_known(self):
        if self.dnd_class in CLASSES_WITH_KNOWN_SPELLS:
            return int(DND5E_DICT["Classes"][self.dnd_class]["Resources"][f"Level {self.level}"]["Spells Known"])
        elif self.dnd_class in CLASSES_WITH_PREPARED_SPELLS:
            if self.dnd_class in INTELLIGENCE_SPELL_CASTERS:
                return self.intelligence_modifier + self.level
            elif self.dnd_class in WISDOM_SPELL_CASTERS:
                return self.wisdom_modifier + self.level
            elif self.dnd_class in CHARISMA_SPELL_CASTERS:
                return self.charisma_modifier + self.level

    @property
    def highest_spell_level_known(self):
        count = 0
        spell_slot_dict = DND5E_DICT["Classes"][self.dnd_class]["Resources"][f"Level {self.level}"]["Spell Slots"]
        for spell_level in spell_slot_dict:
            if spell_slot_dict[spell_level] != "":
                count += 1
        return count

    @property
    def spell_casting_ability_bonus(self):
        if self.dnd_class in INTELLIGENCE_SPELL_CASTERS:
            return self.intelligence_modifier
        elif self.dnd_class in WISDOM_SPELL_CASTERS:
            return self.wisdom_modifier
        elif self.dnd_class in CHARISMA_SPELL_CASTERS:
            return self.charisma_modifier

    @property
    def spell_save_dc(self):
        return 8 + self.proficiency_bonus + self.spell_casting_ability_bonus

    @property
    def spell_attack_bonus(self):
        return self.proficiency_bonus + self.spell_casting_ability_bonus

    def choose_cantrips(self):
        cantrips = DND5E_DICT["Classes"][self.dnd_class]["Spell List"]["Spell Level"]["0"]
        return [choice(cantrips) for _ in range(int(self.number_of_cantrips_known))]

    def choose_spells(self):
        list_of_known_spells = {}
        for spell_level in range(1, self.highest_spell_level_known + 1):
            list_of_known_spells.update({spell_level:[]})
        spells_added = 0
        while spells_added != self.number_of_spells_known:
            for spell_level in list_of_known_spells:
                if spells_added == self.number_of_spells_known:
                    break
                list_of_known_spells[spell_level].append(choice(DND5E_DICT["Classes"][self.dnd_class]["Spell List"]["Spell Level"][str(spell_level)]))
                spells_added += 1
        return list_of_known_spells


class Barbarian(Adventurer):
    def __init__(self):
        super().__init__()

    def rages(self):
        return DND5E_DICT["Classes"][self.dnd_class]["Resources"][f"Level {self.level}"]["Rages"]

    def rage_damage(self):
        return DND5E_DICT["Classes"][self.dnd_class]["Resources"][f"Level {self.level}"]["Rage Damage"]


class Bard(SpellCaster):
    def __init__(self):
        super().__init__()
        self.known_cantrips = self.choose_cantrips()


class Cleric(SpellCaster):
    def __init__(self):
        super().__init__()
        self.known_cantrips = self.choose_cantrips()


class Druid(SpellCaster):
    def __init__(self):
        super().__init__()
        self.known_cantrips = self.choose_cantrips()


class Fighter(Adventurer):
    def __init__(self):
        super().__init__()


class Monk(Adventurer):
    def __init__(self):
        super().__init__()

    def ki_points(self):
        return DND5E_DICT["Classes"][self.dnd_class]["Resources"][f"Level {self.level}"]["Ki Points"]

    def martial_arts(self):
        return DND5E_DICT["Classes"][self.dnd_class]["Resources"][f"Level {self.level}"]["Martial Arts"]

    def unarmored_movement(self):
        return DND5E_DICT["Classes"][self.dnd_class]["Resources"][f"Level {self.level}"]["Unarmored Movement"]


class Paladin(SpellCaster):
    def __init__(self):
        super().__init__()


class Ranger(SpellCaster):
    def __init__(self):
        super().__init__()


class Rogue(Adventurer):
    def __init__(self):
        super().__init__()

    def sneak_attack(self):
        return DND5E_DICT["Classes"][self.dnd_class]["Resources"][f"Level {self.level}"]["Sneak Attack"]


class Sorcerer(SpellCaster):
    def __init__(self):
        super().__init__()
        self.known_cantrips = self.choose_cantrips()

    def sorcery_points(self):
        return DND5E_DICT["Classes"][self.dnd_class]["Resources"][f"Level {self.level}"]["Sorcery Points"]


class Warlock(SpellCaster):
    def __init__(self):
        super().__init__()
        self.known_cantrips = self.choose_cantrips()

    def number_of_invocations_known(self):
        return DND5E_DICT["Classes"][self.dnd_class]["Resources"][f"Level {self.level}"]["Invocations Known"]


class Wizard(SpellCaster):
    def __init__(self):
        super().__init__()
        self.known_cantrips = self.choose_cantrips()


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
