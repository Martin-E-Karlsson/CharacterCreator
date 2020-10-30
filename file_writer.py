from constants import *

def write_character_sheet(bard):
    character = bard
    if character.subrace != "":
        race = character.subrace
    else:
        race = character.race

    racial_bonuses = "".join("%s:\n%s\n\n" % item for item in bard.racial_bonuses.items())
    class_features = "".join("%s:\n%s\n\n" % item for item in bard.class_features.items())
    character_sheet = f"""Name: {character.first_name} {character.last_name}    Class: {character.dnd_class}    Level: {character.level}    Archetype: {character.archetype}

Race: {race}     Background: {character.background}    Alignment: {character.alignment}    Deity: {character.deity}

Ability Scores (Ability Score Bonus):
Strength: {character.strength} ({character.strength_modifier})        Dexterity: {character.dexterity} ({bard.dexterity_modifier})    Constitution: {bard.constitution} ({bard.constitution_modifier})    
Intelligence: {bard.intelligence} ({bard.intelligence_modifier})    Wisdom: {bard.wisdom} ({bard.wisdom_modifier})       Charisma: {bard.charisma} ({bard.charisma_modifier})

Hit Points: {bard.max_hit_points}    Hit Die: {bard.hit_die}    Initiative: {bard.initiative_bonus}    Speed: {bard.speed}    
Passive Perception: {bard.passive_perception}    Proficiency Bonus: {bard.proficiency_bonus}    Inspiration: {bard.inspiration}

Saving Throws:
Strength: {bard.strength_save_bonus}    Dexterity: {bard.dexterity_save_bonus}    Constitution: {bard.constitution_save_bonus}
Intelligence: {bard.intelligence_save_bonus}    Wisdom: {bard.wisdom_save_bonus}    Charisma: {bard.charisma_save_bonus}

Skill bonus:
Athletics: {bard.athletics_bonus}    Acrobatics: {bard.acrobatics_bonus}    Sleight of Hand: {bard.sleight_of_hand_bonus}    Stealth: {bard.stealth_bonus}    Arcana: {bard.arcana_bonus}
History: {bard.history_bonus}    Investigation: {bard.investigation_bonus}    Nature: {bard.nature_bonus}    Religion: {bard.religion_bonus}    Animal Handling: {bard.animal_handling_bonus}
Insight: {bard.insight_bonus}    Medicine: {bard.medicine_bonus}    Perception: {bard.perception_bonus}    Survival: {bard.survival_bonus}    Deception: {bard.deception_bonus}    
Intimidation: {bard.intimidation_bonus}    Performance: {bard.performance_bonus}    Persuasion: {bard.persuasion_bonus}

Proficiencies:
Armors: {", ".join(bard.armor_proficiencies)}
Weapons: {", ".join(bard.weapon_proficiencies)}
Tools: {", ".join(bard.tool_proficiencies)}

Languages: {", ".join(bard.languages)}

Physical Description:
Age: {bard.age}    Gender: {bard.gender}    Size: {bard.size}    Height: {bard.height}    Weight: {bard.weight}    
Skin Color: {bard.skin_color}    Hair Color: {bard.hair_color}    Eye Color: {bard.eye_color}    
Accent: {bard.accent}    Voice Type: {bard.voice_type}    Memorable Trait : {bard.memorable_trait}

"""
    if bard.dnd_class in SPELL_CASTING_CLASSES:
        known_spells = "".join(f"{CARDINAL_TO_ORDINAL_NUMBERS[key]}: {', '.join(value)}\n" for key, value in bard.known_spells.items())
        spell_slots = "".join(f"{key}: {', '.join(value)}    " for key, value in bard.spell_slots.items())
        character_sheet += f"""Spell Save DC: {bard.spell_save_dc}    Spell Attack Bonus: {bard.spell_attack_bonus}

Spell Slots: 
{spell_slots}
"""
        if bard.dnd_class in CLASSES_WITH_CANTRIPS:
            character_sheet += f"""
Known Cantrips:
{", ".join(bard.known_cantrips)}
"""
        character_sheet += f"""
Known/Prepared Spells:
{known_spells}
"""
    character_sheet += f"""
Features & Traits:
{racial_bonuses}{class_features}
"""

    with open(f"characters/{bard.first_name + '_' + bard.last_name}.txt", "w") as text_file:
        text_file.write(character_sheet)