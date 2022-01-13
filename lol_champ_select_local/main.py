import requests
from requests.models import HTTPBasicAuth
import json
import logging
import time

from get_lockfile_data import get_lockfile_data
from load_team_and_players import load_teams_and_players
from load_splasharts import load_splasharts


def get_champ_select_call(port, key):
    headers = {'Accept': 'application/json'}
    return requests.get('https://127.0.0.1:'+ port +'/lol-champ-select/v1/session', headers=headers, auth=HTTPBasicAuth('riot', key), verify=False)


if __name__ == "__main__":
    lockfile_data = get_lockfile_data()
    
    wait_time = 1
    
    while(True):
        res = get_champ_select_call(lockfile_data['port'], lockfile_data['key'])

        if res.status_code != 200:
            logging.info('Didnt get champ select data')
            time.sleep(3)
        else:
            wait_time = 1
            cs_data = str(res.content)
            cs_data = cs_data[str.index(cs_data, '{'):]
            cs_data = str.replace(cs_data, '\\\'', '')
            cs_data = cs_data[:len(cs_data)-1]
            cs_dict = json.loads(cs_data)

            load_teams_and_players(cs_dict)
            load_splasharts(cs_dict)

            time.sleep(10)
