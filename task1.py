from pprint import pprint

import requests


def get_superhero_id(name):
    base_url = "https://superheroapi.com/api/2619421814940190/"
    search_url = f'{base_url}search/{name}'
    response = requests.get(search_url)
    data = response.json()
    superhero_id = data['results'][0]['id']
    return superhero_id


superheros = ['Hulk', 'Captain America', 'Thanos']


def get_superhero_intelligence(id):
    base_url = "https://superheroapi.com/api/2619421814940190/"
    powerstats_url = f'{base_url}{id}/powerstats'
    response = requests.get(powerstats_url)
    data = response.json()
    intelligence = int(data['intelligence'])
    return intelligence


max_intelligence = 0
smartest_superhero = ''

for superhero in superheros:
    superhero_id = get_superhero_id(superhero)
    intelligence = get_superhero_intelligence(superhero_id)

    if intelligence > max_intelligence:
        max_intelligence = intelligence
        smartest_superhero = superhero

print(f'Самый умный герой: {smartest_superhero}')
