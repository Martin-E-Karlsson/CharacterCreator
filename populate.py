import json
# import PySimpleGUI as sg


def add_value(json_data, path, value):
    for key in path[:-1]:
        json_data = json_data.setdefault(key, {})

    # json_data[path[-1]].update(value)
    json_data[path[-1]] = value
    # return json_data


def add_values_to_classes(json_data, path):
    for key in json_data["Class"].keys():
        values_list = []
        count = 0
        while True:
            count += 1
            new_value = input(f"{key} {path[-1]} Value #{count}: ")
            if new_value != "":
                values_list.append(new_value)
            else:
                break

        add_value(json_data, ["Class", key, path[0]], {path[1]: values_list})

    return json_data


def add_empty_dict(json_data, path):
    for key in json_data["Class"].keys():
        values_list = []
        count = 0
        while True:
            count += 1
            new_value = input(f"{key} {path[-2]} {path[-1]}, value #{count}: ")
            if new_value != "":
                values_list.append(new_value)
            else:
                break

        json_data["Class"][key][path[0]].setdefault(path[1], {})
        for value in values_list:
            json_data["Class"][key][path[0]][path[1]].update({value: ""})
            # add_value(json_data, ["Class", key, path[0], path[1]], {value: ""})
    return json_data


def add_list_to_classes(json_data, path):
    for key in json_data["Class"].keys():
        new_value = input(f"{key} {path[-1]}: ")
        add_value(json_data, ["Class", key, path[0]], {path[1]: new_value.split(", ")})
    return json_data


def add_resource_dicts_to_classes(json_data):
    for class_key in json_data["Class"].keys():
        json_data["Class"][class_key].setdefault("Resources", {})
        for level in range(1, 21):
            json_data["Class"][class_key]["Resources"][f"Level {level}"] = {}
        count = 0
        while True:
            count += 1
            input_value = input(f"{class_key} Resource Type #{count}: ")
            if input_value != "":
                if input_value == "Spell Slots":
                    for level in json_data["Class"][class_key]["Resources"].keys():
                        json_data["Class"][class_key]["Resources"][level].setdefault(input_value, {})
                        json_data["Class"][class_key]["Resources"][level][input_value].setdefault("1st", input(
                            f"{class_key}, {level}, # of 1st level spell slots: "))
                        json_data["Class"][class_key]["Resources"][level][input_value].setdefault("2nd", input(
                            f"{class_key}, {level}, # of 2nd level spell slots: "))
                        json_data["Class"][class_key]["Resources"][level][input_value].setdefault("3rd", input(
                            f"{class_key}, {level}, # of 3rd level spell slots: "))
                        json_data["Class"][class_key]["Resources"][level][input_value].setdefault("4th", input(
                            f"{class_key}, {level}, # of 4th level spell slots: "))
                        json_data["Class"][class_key]["Resources"][level][input_value].setdefault("5th", input(
                            f"{class_key}, {level}, # of 5th level spell slots: "))
                        json_data["Class"][class_key]["Resources"][level][input_value].setdefault("6th", input(
                            f"{class_key}, {level}, # of 6th level spell slots: "))
                        json_data["Class"][class_key]["Resources"][level][input_value].setdefault("7th", input(
                            f"{class_key}, {level}, # of 7th level spell slots: "))
                        json_data["Class"][class_key]["Resources"][level][input_value].setdefault("8th", input(
                            f"{class_key}, {level}, # of 8th level spell slots: "))
                        json_data["Class"][class_key]["Resources"][level][input_value].setdefault("9th", input(
                            f"{class_key}, {level}, # of 9th level spell slots: "))
                else:
                    for level in json_data["Class"][class_key]["Resources"].keys():
                        json_data["Class"][class_key]["Resources"][level].setdefault(input_value, input(f"{input_value} value {level}: "))
            else:
                break
        for level in json_data["Class"][class_key]["Resources"].keys():
            print(level)
            for key, value in json_data["Class"][class_key]["Resources"][level].items():
                print(key, ' : ', value)
    return json_data


def fetch_value(data, keys):
    return fetch_value(data[keys[0]], keys[1:]) \
        if keys else data


def run():
    with open('dnd5e.json', encoding='utf-8') as f:
        json_data = json.load(f)

    # print(json_data["Class"]["Cleric"]["Features"]["Level 5"]["Destroy Undead"])
    # print(json_data["Class"]["Druid"]["Features"]["Level 2"]["Wild Shape"])
    # print(json_data["Class"]["Rogue"]["Features"]["Level 1"]["Expertise"])

    # data_out = add_list_to_classes(data_in, ["Proficiencies", "Skills"])

    # add_resource_dicts_to_classes(json_data)

    # for i in range(1, 21):
    #     add_empty_dict(json_data, ["Features", f"Level {i}"])

    # add_empty_dict(json_data, ["Class", "Barbarian", "Features"], {"Features": {"Level 1": {}}})

    # test_dict = add_list_to_classes(data_in, ["Features", "Level 1"])

    with open('dnd5e.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, sort_keys=True)


def main():
    run()


if __name__ == '__main__':
    main()
