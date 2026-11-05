import requests
from dotenv import load_dotenv
import os


def load_data(requested_animal):
  """ Loads all data from animal API """
  load_dotenv()
  url = "https://api.api-ninjas.com/v1/animals"

  headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-Api-Key": os.getenv('API_KEY')
  }

  response = requests.get(f"https://api.api-ninjas.com/v1/animals?name={requested_animal}", headers=headers)
  return response.json()


def key_present_in_dictionary(key, dictionary):
  return key in dictionary


def get_animals_infos_json_as_string(json_string ):
  output=""
  for item in json_string:
    output += serialize_animal(item)
  return output


def serialize_animal(animal_obj):
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
  return input("Enter a name of an animal: ")


json_animals_infos_string = load_data(get_users_input())
with open("animals_template.html", "r", encoding="utf-8") as handle:
  html_original_string = handle.read()

html_filled_wih_infos_as_string = html_original_string.replace("            __REPLACE_ANIMALS_INFO__", get_animals_infos_json_as_string(json_animals_infos_string))

with open("animals.html", "w", encoding="utf-8") as handle:
  handle.write(html_filled_wih_infos_as_string)