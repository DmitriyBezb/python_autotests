import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'user_token'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}
TRAINER_ID = '30238'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_piece_of_response():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.json()['data'][0]['city'] == 'Budapest'

@pytest.mark.parametrize('key,value' , [('city' , 'Budapest'),('id' , TRAINER_ID),('trainer_name' , 'Vilhelm')])
def test_params(key, value):
    responce_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert responce_parametrize.json()['data'][0][key] == value