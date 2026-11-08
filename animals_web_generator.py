import data_fetcher

def load_data(requested_animal):
    """animals api is queried with the provided animal name and complete response is returned"""
    return data_fetcher.fetch_data(requested_animal)


def key_present_in_dictionary(key, dictionary):
    """simple check to make code is more readable"""
    return key in dictionary


def get_animals_infos_json_as_string(json_string ):
    """given a complete josn as string the function builds a complete string representing html of a complete list of list items and returns it"""
    output=""
    for item in json_string:
        output += serialize_animal(item)
    return output


def serialize_animal(animal_obj):
    """provided an animal object, the function builds a string for 1 list element in html with data from that object. The string is then used in the result html"""
    output = ""
    output += "\t\t\t<li class=\"cards__item\">\n"
    output += f"\t\t\t\t<div class=\"card__title\">{animal_obj["name"]}</div>\n"
    output += "\t\t\t\t\t<p class=\"card__text\">"
    output += f"<strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n"
    output += f"\t\t\t\t\t<strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n"

    if key_present_in_dictionary("type", animal_obj["characteristics"]):
        output += f"\t\t\t\t\t<strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n"
    output += "\t\t\t\t</p>\n"
    output += "\t\t\t</li>\n"
    return output


def get_users_input():
    """users input will be used as a query parameter for the call to animal api"""
    return input("Enter a name of an animal: ")


def main():
    json_animals_infos_string = load_data(get_users_input())
    with open("animals_template.html", "r", encoding="utf-8") as handle:
        html_original_string = handle.read()

    html_filled_wih_infos_as_string = html_original_string.replace("            __REPLACE_ANIMALS_INFO__", get_animals_infos_json_as_string(json_animals_infos_string))

    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(html_filled_wih_infos_as_string)


if __name__ == "__main__":
    main()