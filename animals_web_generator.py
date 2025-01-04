import data_fetcher as d_f


def bring_animals_to_html(list_of_cards):
    """
    here the placeholder is replaced by the actual new animal list
    created in building_all_cards
    """
    with open('animals_template.html',"r")as file:
      page = file.read()
    new_html=page.replace("__REPLACE_ANIMALS_INFO__", list_of_cards)
    with open ("animals.html", "w") as file:
        file.write(new_html)
        return "animals.html"


def errormassage(nonanimal):
    """
    in case the users input doesn´t exist,
    this function prints it on the screen
    """
    output = ''
    output += (f'<li class="cards__item "><center><h2>The animal "{nonanimal}" does not exist.</h2>'
               f'<h2>At least not in this data bank.</h2></center></li>\n')
    print(bring_animals_to_html(output))


def seralize_animal(obj):
    """
    here every animal gets an own card written
    """
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
    """
    here we add together all animal cards to on file
    """
    output = ""
    for animal in range(len(cards)):
        output += seralize_animal(cards[animal])
    return output


def main():
    """
    in the main is not only organised, that the functions work together,
    it also organises error handling by wrong user input
    """
    animal_name = input("Enter a name of an animal: ")
    animals_data = d_f.fetch_data(animal_name)
    if animals_data==[]:
        errormassage(animal_name)
        print(f"{animal_name} is not in the database.")
    else:
        animal_on_card = building_all_cards(animals_data)
        bring_animals_to_html(animal_on_card)
        print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
