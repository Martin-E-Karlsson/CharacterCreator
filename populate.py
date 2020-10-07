import json
# import PySimpleGUI as sg


def add_value(json_data, path, value):
    for key in path[:-1]:
        json_data = json_data.setdefault(key, {})

    json_data[path[-1]].update(value)
    return json_data


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


def fetch_value(data, keys):
    return fetch_value(data[keys[0]], keys[1:]) \
        if keys else data


def run():
    with open('dnd5e.json') as f:
        data_in = json.load(f)

    data_out = add_values_to_classes(data_in, ["Proficiencies", "Weapons"])

    with open('dnd5e.json', 'w') as f:
        json.dump(data_out, f, indent=2, sort_keys=True)


def main():
    run()


if __name__ == '__main__':
    main()
