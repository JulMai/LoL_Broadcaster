from requests.models import HTTPBasicAuth
import requests
import os
import json
import logging


def get_lockfile_data():
    lol_path_default = "C:\\Riot Games\\League of Legends\\"

    if os.path.exists(lol_path_default):
        lol_path = lol_path_default
    else:
        pass

    if os.path.isfile(lol_path + "\\lockfile"):
        lockfile_path = lol_path + "\\lockfile"


    with open(lockfile_path) as f:
        line = f.readline()
        line = str.replace(line, "LeagueClient:", "")
        line = str.replace(line, ":https", "")
        line = line[(str.index(line, ":")+1):len(line)]
        port = line[0:str.index(line, ":")]
        key = line[(str.index(line, ":")+1):]
    
    return {"port": port, "key": key}


def get_champ_select_call(port, key):
    headers = {'Accept': 'application/json'}
    return requests.get('https://127.0.0.1:'+ port +'/lol-champ-select/v1/session', headers=headers, auth=HTTPBasicAuth('riot', key), verify=False)

if __name__ == '__main__':
    lockfile_data = get_lockfile_data()
    
    wait_time = 1
    
    while(True):
        res = get_champ_select_call(lockfile_data['port'], lockfile_data['key'])
        
        if res.status_code != 200:
            wait_time = 10
            logging.info('Didnt get champ select data')
        else:
            wait_time = 1
            cs_data = str(res.content)
            cs_data = cs_data[str.index(cs_data, '{'):]
            cs_data = str.replace(cs_data, '\\\'', '')
            cs_data = cs_data[:len(cs_data)-1]
            cs_dict = json.loads(cs_data)
            
            print("")