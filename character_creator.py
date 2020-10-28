from character import Character, Adventurer


class Creator:  # TODO: To contain the core loop of the program
    def __init__(self):
        pass


def run():
    new_char = Adventurer()
    attributes = vars(new_char)
    print("".join("%s: %s\n" % item for item in attributes.items()))
    # divider = "\n" + "-" * 150 + "\n"
    # print("".join(f"%s: %s{divider}" % item for item in new_char.class_features.items()))


def main():
    run()


if __name__ == '__main__':
    main()
