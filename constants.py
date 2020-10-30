""" A storage space for external data and constants used in CharacterCreator. """
import json

with open('dnd5e.json', encoding='utf-8') as f:
    DND5E_DICT = json.load(f)

RACES = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc", "Halfling", "Human", "Tiefling"]
GENDERS = ["Male", "Female"]

LIGHT_BASIC_SKIN_COLORS = ["Pale", "Light", "Light Tan", "Tan",]
DARK_BASIC_SKIN_COLORS = ["Dark Tan", "Brown", "Dark Brown", "Black"]
BASIC_SKIN_COLORS = LIGHT_BASIC_SKIN_COLORS + DARK_BASIC_SKIN_COLORS
EXOTIC_SKIN_COLORS = ["Bronze", "Copper", "Alabaster", "Light Blue"]
BASIC_EYE_COLORS = ["Amber", "Blue", "Brown", "Gray", "Green", "Hazel", "Red", "Violet", "Aqua Marine", "Yellow"]
EXOTIC_EYE_COLORS = ["Golden", "Silver", "Black"]
BASIC_HAIR_COLORS = ["Blue Black", "Black", "Dark Brown", "Brown", "Light Brown", "Chestnut Brown", "Auburn", "Red",
                     "Copper", "Orange Brown", "Strawberry Blond", "Light Blond", "Golden Blond", "Medium Blond",
                     "Grey", "White"]
EXOTIC_HAIR_COLORS = ["Blue-White", "Blue", "Green", "Golden Blond", "Silver-White"]

HIGH_ELF_HAIR_COLORS = ["Copper", "Black", "Golden Blond", "Silver-White", "Blue"]
HIGH_ELF_SKIN_COLORS = ["Bronze", "Copper", "Alabaster", "Light Blue"]
DARK_ELF_EYE_COLORS = ["Lilac", "Silver", "Pink", "Red", "Blue"]
DARK_ELF_HAIR_COLORS = ["Stark White", "Pale Yellow"]
DEEP_GNOME_SKIN_COLORS = ["Brown", "Black", "Gray"]
HALF_ORC_SKIN_COLORS = ["Light Gray", "Pale Green"]
TIEFLING_SKIN_COLORS = BASIC_SKIN_COLORS + ["Light Red", "Red", "Dark Red"]
TIEFLING_EYE_COLORS = ["Black", "Red", "White", "Silver", "Gold"]
TIEFLING_HAIR_COLORS = ["Black", "Brown", "Dark Red", "Blue", "Purple"]

ACCENTS = ["British", "Scottish", "Irish", "French", "Italian", "Russian", "German", "Swedish", "Norwegian", "Finnish",
           "Arabic", "Texan", "Italian-American", "Indian", "Japanese", "Australian"]
VOICE_TYPES = ["Deep", "Breathy", "Squeaky", "Monotone", "Tired", "High", "Gravelly", "Hoarse", "Whispery", "Average",
               "Haughty", "Stuttery", "Lispy", "Shouty"]
BACKGROUNDS = ["Acolyte", "Anthropologist", "Archaeologist", "Caravan Specialist", "Charlatan", "City Watch",
               "Cloistered Scholar", "Courtier", "Criminal", "Entertainer", "Far Traveler", "Folk Hero", "Gladiator",
               "Guild Artisan", "Guild Merchant", "Harborfolk", "Hermit", "Investigator", "Knight", "Noble", "Pirate",
               "Sage", "Sailor", "Soldier", "Spy", "Student Of Magic", "Urchin"]
MEMORABLE_TRAITS = ["Bushy Sideburns", "Noticeably Crooked Teeth", "Freckled", "Missing 7th Finger", "Scar Across Nose",
                    "Missing Right Ear", "Impeccably Dressed", "Heavily Perfumed", "Tiny Tattoos All Over Their Face",
                    "Very Shiny Shoes", "Yellow Teeth", "Manicured Hands", "Scarred Forearms", "Toned Leg Muscles"
                    "Slight Unibrow", "Missing Eyebrows", "Full Body Tattoo", "One-Eyed", "Heavily Burned",
                    "Unusually Large Feet", "Distracting Mole", "One Jutting Snaggletooth", "Covered In Scars",
                    "Slightly Radiant", "Impeccable Skin Care", "Heterochromia", "Incredibly Beatiful", "Warm Smile"]

ALIGNMENTS = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral", "Chaotic Neutral",
              "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
LAWFUL_GOOD_DEITIES = ["Aba", "Ilmater", "Torm", "Tyr", "Heimdall", "Athena", "Re-Horakhty", "Osiris", "Diancecht"]
NEUTRAL_GOOD_DEITIES = ["Chauntea", "Deneir", "Eldath", "Lathander", "Mielikki", "Milil", "Mystra", "Odin", "Balder",
                        "Frey", "Freya", "Njord", "Artemis", "Demeter", "Hephaestus", "Hestia", "Hathor", "Imhotep",
                        "Isis", "Belenus", "Brigantia", "Goibhniu", "Oghma"]
CHAOTIC_GOOD_DEITIES = ["Lliira", "Selûne", "Sune", "Tymora", "Odur", "Sif", "Thor", "Aphrodite", "Apollo", "Hercules",
                        "Hermes", "Bast", "Nephthys", "The Daghdha"]
LAWFUL_NEUTRAL_DEITIES = ["Azuth", "Helm", "Kelemvor", "Savras", "Tyr", "Nike", "Anubis", "Ptah", "Thoth", "Manannan"]
TRUE_NEUTRAL_DEITIES = ["Gond", "Oghma", "Silvanus", "Tempus", "Waukeen", "Forseti", "Frigga", "Skadi", "Zeus", "Tyche",
                        "Arawn", "Dunatis", "Nuada", "Silvanus"]
CHAOTIC_NEUTRAL_DEITIES = ["Mask", "Leira", "Hermod", "Uller", "Dionysus", "Hera", "Pan", "Poseidon", "Bes", "Lugh"]
LAWFUL_EVIL_DEITIES = ["Bane", "Loviatar", "Surtur", "Hades", "Sobek"]
NEUTRAL_EVIL_DEITIES = ["Auril", "Bhaal", "Myrkul", "Shar", "Aegir", "Hel", "Apep", "Math Mathonwy"]
CHAOTIC_EVIL_DEITIES = ["Cyric", "Beshaba", "Malar", "Talona", "Talos", "Umberlee", "Loki", "Thrym", "Ares", "Hecate",
                        "Set", "Morrigan"]

CLASSES = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer",
           "Warlock", "Wizard"]
CLASS_ABILITY_SCORE_PRIORITY = {
    "Barbarian": ["Str", "Con", "Dex", "Wis", "Cha", "Int"],
    "Bard": ["Cha", "Dex", "Con", "Wis", "Str", "Int"],
    "Cleric": ["Wis", "Con", "Str", "Dex", "Cha", "Int"],
    "Druid": ["Wis", "Con", "Dex", "Int", "Cha", "Str"],
    "Fighter": ["Str", "Con", "Dex", "Wis", "Cha", "Int"],
    "Monk": ["Dex", "Wis", "Con", "Str", "Cha", "Int"],
    "Paladin": ["Str", "Con", "Dex", "Cha", "Wis", "Int"],
    "Ranger": ["Dex", "Con", "Wis", "Str", "Cha", "Int"],
    "Rogue": ["Dex", "Con", "Cha", "Wis", "Int", "Str"],
    "Sorcerer": ["Cha", "Con", "Dex", "Wis", "Int", "Str"],
    "Warlock": ["Cha", "Con", "Dex", "Wis", "Str", "Int"],
    "Wizard": ["Int", "Dex", "Con", "Wis", "Cha", "Str"]
}
SPELL_CASTING_CLASSES = ["Bard", "Cleric", "Druid", "Paladin", "Ranger", "Sorcerer", "Warlock", "Wizard"]
CLASSES_WITH_CANTRIPS = ["Bard", "Cleric", "Druid", "Sorcerer", "Warlock", "Wizard"]
CLASSES_WITH_KNOWN_SPELLS = ["Bard", "Ranger", "Sorcerer", "Warlock"]
CLASSES_WITH_PREPARED_SPELLS = ["Cleric", "Druid", "Paladin", "Wizard"]
CARDINAL_TO_ORDINAL_NUMBERS = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "6th", 7: "7th", 8: "8th", 9: "9th"}
ORDINAL_TO_CARDINAL_NUMBERS = {"1st": 1, "2nd": 2, "3rd": 3, "4th": 4, "5th": 5, "6th": 6, "7th": 7, "8th": 8, "9th": 9}
INTELLIGENCE_SPELL_CASTERS = ["Wizard"]
WISDOM_SPELL_CASTERS = ["Cleric", "Druid", "Ranger"]
CHARISMA_SPELL_CASTERS = ["Bard", "Paladin", "Sorcerer", "Warlock"]