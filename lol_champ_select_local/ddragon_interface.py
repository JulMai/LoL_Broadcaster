import requests
import json


def load_champions():
    url = 'http://ddragon.leagueoflegends.com/cdn/11.24.1/data/en_US/champion.json'
    response = requests.get(url)
    return json.loads(response.content)['data']


def get_champinfo(champ_id):
    champions = load_champions()
    print("")
    
def get_champName(champ_id):
    champions = load_champions()

    for name in champions:
        if champ_id == int(champions[name]['key']):
            return name
    return 'Doesn\'t exist'

def get_splashart_url(name):
    return 'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{0}_0.jpg'.format(name)

if __name__ == '__main__':
    print(get_champName(105))
