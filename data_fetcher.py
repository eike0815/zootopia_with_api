import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')
headers = {'X-Api-Key': API_KEY}
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
    url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    req =requests.get(url, headers = headers)
    return req.json()


#print(fetch_data("turtle")) #this is here for testing