# All constant variables are stored here.
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
