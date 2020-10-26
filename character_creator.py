from character import Character


class Creator:  # TODO: To contain the core loop of the program
    def __init__(self):
        pass


def run():
    new_character = Character()
    print(new_character.race)
    print(new_character.gender)
    print(new_character.first_name + " " + new_character.last_name)


def main():
    run()


if __name__ == '__main__':
    main()
