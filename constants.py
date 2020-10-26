# All constant variables are stored here.
import json

with open('dnd5e.json', encoding='utf-8') as f:
    DND5E_DICT = json.load(f)

RACES = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc", "Halfling", "Human", "Tiefling"]
GENDERS = ["Male", "Female"]