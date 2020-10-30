from character import Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard, Adventurer
from file_writer import write_character_sheet
from constants import CLASSES
from random import choice


def run():
    random_class = choice(CLASSES)
    class_to_adventurer = {"Barbarian": Barbarian, "Bard": Bard, "Cleric": Cleric, "Druid": Druid, "Fighter": Fighter,
                           "Monk": Monk, "Paladin": Paladin, "Ranger": Ranger, "Rogue": Rogue, "Sorcerer": Sorcerer,
                            "Warlock": Warlock, "Wizard": Wizard}
    random_class_reference = class_to_adventurer.get(random_class, Adventurer)
    random_adventurer = random_class_reference()
    write_character_sheet(random_adventurer)


def main():
    run()


if __name__ == '__main__':
    main()
