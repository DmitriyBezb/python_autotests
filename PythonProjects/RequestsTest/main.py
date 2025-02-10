import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'user_token'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}
born = {"name": "Самсон", "photo_id": 47}
name = {"pokemon_id": "226437", "name": "Ringo", "photo_id": 17}
catch = {"pokemon_id": "226437"}

response_born = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = born) 
print(response_born.text)

#responce_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = name) 
#print(responce_name.text)

#responce_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = catch) 
#print(responce_catch.text)

#pokemon_id = response_born.json()['id'] 
#print(response_born.text)