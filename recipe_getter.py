import requests

SPOON_API = 'd273602d639945afb3ca152e75d82d91'


def get_raw_answer(*ingridients_raw):
    ingredients = ingridients_raw[0]
    for i in range(1, len(ingridients_raw)):
        ingredients += ',+' + ingridients_raw[i]
    print(ingredients)
    url = f'https://api.spoonacular.com/recipes/findByIngredients?apiKey={SPOON_API}&ingredients={ingredients}'
    response = requests.get(url)
    print(response.text)
    return response.text


get_raw_answer('apples', 'flour', 'sugar')