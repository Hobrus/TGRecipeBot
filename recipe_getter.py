import requests
import json

SPOON_API = 'd273602d639945afb3ca152e75d82d91'


def get_raw_answer_ids(*ingridients_raw):
    ingredients = ingridients_raw[0]
    for i in range(1, len(ingridients_raw)):
        ingredients += ',+' + ingridients_raw[i]
    print(ingredients)
    url = f'https://api.spoonacular.com/recipes/findByIngredients?apiKey={SPOON_API}&ingredients={ingredients}'
    response = requests.get(url)
    print(response.text)
    return response.text


def parse_answer_for_ids(text):
    recipes = json.loads(text)
    recipe_ids = []
    for recipe in recipes:
        recipe_ids.append(recipe['id'])
    return recipe_ids


def get_raw_answer_recipes(*ids):
    ingredients = ingridients_raw[0]
    for i in range(1, len(ingridients_raw)):
        ingredients += ',+' + ingridients_raw[i]
    print(ingredients)
    url = f'https://api.spoonacular.com/recipes/{id}/information?apiKey={SPOON_API}'
    response = requests.get(url)
    print(response.text)
    return response.text

print(parse_answer(get_raw_answer('egg', 'sugar')))