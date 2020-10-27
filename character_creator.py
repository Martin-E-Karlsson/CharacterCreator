from character import Character


class Creator:  # TODO: To contain the core loop of the program
    def __init__(self):
        pass


def run():
    new_character = Character()
    if new_character.subrace:
        print(new_character.subrace)
    else:
        print(new_character.race)
    print(new_character.gender)
    print(new_character.first_name + " " + new_character.last_name)
    print(new_character.age)
    print(new_character.size)
    print(new_character.height)
    print(new_character.weight)
    print(new_character.skin_color)
    print(new_character.hair_color)
    print(new_character.eye_color)
    print(new_character.accent)
    print(new_character.voice_type)
    print(new_character.background)
    print(new_character.memorable_trait)
    print(new_character.languages)
    print(new_character.alignment)
    print(new_character.deity)


def main():
    run()


if __name__ == '__main__':
    main()
