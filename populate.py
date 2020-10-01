import json


def main():
    # classes_string = '''
    # {
    #     "classes": [
    #         "Barbarian",
    #         "Bard",
    #         "Cleric",
    #         "Druid",
    #         "Fighter",
    #         "Monk",
    #         "Paladin",
    #         "Ranger",
    #         "Rogue",
    #         "Sorcerer",
    #         "Warlock",
    #         "Wizard"
    #     ]
    # }
    # '''

    with open('dnd5e.json') as f:
        data = json.load(f)

    # data = json.loads(classes_string)
    # print(data)
    # print(type(data))

    # for i, c in enumerate(data['classes']):
    #     data['classes'][i] = 'Gnome ' + c
    #
    # new_string = json.dumps(data, indent=2)
    #
    # print(new_string)
    #
    # with open('gnome_classes.json', 'w') as f:
    #     json.dump(data, f, indent=2)

    for c in data['classes']:
        # print(f"{c} has the hit die {data['classes'][c]['Hit Die']}")
        # data['classes'][c]['Saves'] = ['Strength', 'Constitution']
        data['classes'][c]['Saves'].sort()

    with open('dnd5e.json', 'w') as f:
        json.dump(data, f, indent=2, sort_keys=True)


if __name__ == '__main__':
    main()
