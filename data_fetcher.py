from dotenv import load_dotenv
import os
import requests
import json

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  """ Loads all data from animal API """
  load_dotenv()
  url = "https://api.api-ninjas.com/v1/animals?name="
  API_KEY = os.getenv('API_KEY')
  headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-Api-Key": API_KEY
  }

  response = requests.get(f"{url}{animal_name}", headers=headers)

  return response.json()