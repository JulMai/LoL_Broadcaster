import os
from pathlib import Path
from urllib.request import urlretrieve

from ddragon_interface import get_champName, get_splashart_url

def get_pic_path(cellId):
    path = "{0}\\Pictures\\Champselect_Pictures\\slot{1}.jpg".format(Path.home(), cellId)
    if not os.path.isfile(path):
        Path("{0}\\Pictures\\Champselect_Pictures\\".format(Path.home())).mkdir(parents=True, exist_ok=True)
    return path

def save_pic_from_url_to(url, save_to):
    urlretrieve(url, save_to)

def no_champ_pic(path):
    pass

def load_splasharts(cs_dict):
    for a in cs_dict:
        if a == 'myTeam' or a == 'theirTeam':
            for player in cs_dict[a]:                        
                champId = player['championId']
                if champId != 0:
                    champ_name = get_champName(champId)
                    if champ_name == "Wukong":
                        champ_name = "MonkeyKing"
                    
                    champ_url = get_splashart_url(champ_name)
                    cellId = player['cellId']
                    pic_path = get_pic_path(cellId)
                    save_pic_from_url_to(champ_url, pic_path)                        
                else:
                    cellId = player['cellId']
                    pic_path = get_pic_path(cellId)
                    no_champ_pic(pic_path)