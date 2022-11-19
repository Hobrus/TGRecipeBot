import requests
import json

SPOON_API = 'd273602d639945afb3ca152e75d82d91'


def get_raw_answer_ids(*ingridients_raw):
    ingredients = ingridients_raw[0]
    for i in range(1, len(ingridients_raw)):
        ingredients += ',+' + ingridients_raw[i]
    url = f'https://api.spoonacular.com/recipes/findByIngredients?apiKey={SPOON_API}&ingredients={ingredients}'
    response = requests.get(url)
    return response.text


def parse_answer_for_ids(text):
    recipes = json.loads(text)
    recipe_ids = []
    for recipe in recipes:
        recipe_ids.append(recipe['id'])
    return recipe_ids


def get_url_recipes(*ids):
    list_urls = []
    for id in ids[0]:
        url = f'https://api.spoonacular.com/recipes/{id}/information?apiKey={SPOON_API}'
        response = requests.get(url)
        recipes = json.loads(response.text)
        url = recipes['sourceUrl']
        list_urls.append(url)
    return list_urls


def get_urls_from_ingridients(*ingridients_raw):
    raw_answer = get_raw_answer_ids(*ingridients_raw)
    ids = parse_answer_for_ids(raw_answer)
    urls = get_url_recipes(ids)
    return urls
