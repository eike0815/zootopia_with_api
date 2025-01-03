import requests


def bring_animals_to_html(list_of_cards):
    """here the placeholder is replaced by the actual new animal list created in building_all_cards"""
    with open('animals_template.html',"r")as file:
      page = file.read()
    new_html=page.replace("__REPLACE_ANIMALS_INFO__", list_of_cards)
    with open ("animals.html", "w") as file:
        file.write(new_html)
        return "animals.html"


def errormassage(nonanimal):
    output = ''
    output += f'<h2>The animal "{nonanimal}" does not exist.</h2>\n'
    print(bring_animals_to_html(output))


headers = {'X-Api-Key':'ghXsb9qIIh5zbZmr8OPrsA==v6sOcmQJCGmeKR5T'}
def load_data(name):
    url = f'https://api.api-ninjas.com/v1/animals?name={name}'
    req =requests.get(url, headers = headers)
    #res = requests.get(url_country_list)#
    return req.json()


def seralize_animal(obj):
    """here every fox gets an own card written """
    output = ''
    output += '<li class="cards__item">\n'
    try:
        output += f'<div class="card_title"><strong>Name:</strong> {obj["name"]}</div>\n'
    except KeyError:
        pass
    output += '<p class="card__text">'
    try:
        output += f'<strong>Diet:</strong> {obj["characteristics"]["diet"]}<br/>\n'
    except KeyError:
        pass
    try:
        lieus = ""
        for lieu in range(0,len(obj["locations"])):
            lieus += obj["locations"][lieu]+" "
        output += f'<strong>Location:</strong> {lieus}<br/>\n'
    except KeyError:
        pass
    try:
        output += f'<strong>Type:</strong> {obj["characteristics"]["type"]}<br/>\n'
    except KeyError:
        pass
    output += '</p>'
    output += '</li>'
    return output


def building_all_cards(cards):
    """here we add together all animal cards to on file"""
    output = ""
    for animal in range(len(cards)):
        output += seralize_animal(cards[animal])
    return output


def main():
    animal_name = input("Enter a name of an animal: ")
    animals_data = load_data(animal_name)
    if animals_data==[]:
        errormassage(animal_name)
        print(f"{animal_name} is not in the database.")
    else:
        animal_on_card = building_all_cards(animals_data)
        bring_animals_to_html(animal_on_card)
        print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
