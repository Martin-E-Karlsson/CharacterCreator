from character import Character, Adventurer, Bard, SpellCaster


def run():
    new_char = SpellCaster()
    attributes = vars(new_char)
    print("".join("%s: %s\n" % item for item in attributes.items()))


def main():
    run()


if __name__ == '__main__':
    main()
