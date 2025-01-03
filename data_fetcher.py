import requests


headers = {'X-Api-Key':'ghXsb9qIIh5zbZmr8OPrsA==v6sOcmQJCGmeKR5T'}
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


#load_data("turtle")