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


def fetch_value(data, keys):
    return fetch_value(data[keys[0]], keys[1:]) \
        if keys else data


def run():  # TODO: Add more values.
    with open('dnd5e.json') as f:
        json_data = json.load(f)

    # data_out = add_list_to_classes(data_in, ["Proficiencies", "Skills"])

    for key in json_data["Class"].keys():
        json_data["Class"][key].setdefault("Features", {})

    for i in range(1, 21):
        add_empty_dict(json_data, ["Features", f"Level {i}"])

    print(json_data)

    # add_empty_dict(json_data, ["Class", "Barbarian", "Features"], {"Features": {"Level 1": {}}})

    # test_dict = add_list_to_classes(data_in, ["Features", "Level 1"])

    # with open('dnd5e.json', 'w') as f:
    #     json.dump(data_out, f, indent=2, sort_keys=True)


def main():
    run()


if __name__ == '__main__':
    main()
