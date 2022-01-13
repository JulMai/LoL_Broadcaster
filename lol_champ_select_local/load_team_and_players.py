from pathlib import Path
import os
import json
from shutil import copy

def get_team_logos_path():
    path = "{0}\\Pictures\\MSI_2021_Teams\\".format(Path.home())
    if not os.path.isfile(path):
        Path("{0}\\Pictures\\MSI_2021_Teams\\".format(Path.home())).mkdir(parents=True, exist_ok=True)
    return path

def load_teams_from_file():
    with open(get_team_logos_path() + "weihnachtsturnier_21_teams.json") as f:
        teams = json.load(f)
    return teams

def get_team_logo_path(file_name):
    return get_team_logos_path() + file_name

def get_summoner_team(teams, id):
    for x in teams:
        for player in teams[x]['player'].values():
            if 'summonerId' in player:
                if player['summonerId'] == id:
                    return teams[x]
    return None
        
def get_team1_live_logo_path():
    return "{0}\\Pictures\\MSI_2021_Teams\\live\\team1.png".format(Path.home())

def get_team2_live_logo_path():
    return "{0}\\Pictures\\MSI_2021_Teams\\live\\team2.png".format(Path.home())

def get_playername_file_path(cellId):
    return "{0}\\Pictures\\MSI_2021_Teams\\live\\summoner{1}.txt".format(Path.home(), cellId)

def load_playernames_for_team(team, team_1_or_2):
    x = (team_1_or_2 - 1) * 3
    for i in range(x + 0, x + 3):
        f = open(get_playername_file_path(i), "w")
        f.write(str(team['player'][str(i - x + 1)]['gamertag']))
        f.close()

def load_teams(team1, team2):
    if len(team1)>0:
        copy(get_team_logos_path() + team1["logo"], get_team1_live_logo_path())
        load_playernames_for_team(team1, 1)
    if len(team2) > 0:
        copy(get_team_logos_path() + team2["logo"], get_team2_live_logo_path())
        load_playernames_for_team(team2, 2)
    


def load_teams_and_players(cs_dict):

    teams = load_teams_from_file()

    team1 = {}
    team2 = {}

    for a in cs_dict:
        if a == 'myTeam' or a == 'theirTeam':
            for player in cs_dict[a]: 
                summonerId = player["summonerId"]
                team = get_summoner_team(teams, summonerId)
                if not team is None:
                    if a == 'myTeam':
                        team1 = team
                    elif a == 'theirTeam':
                        team2 = team
                
    load_teams(team1, team2)
                

if __name__ == '__main__':
    teams = load_teams_from_file()
    team = get_summoner_team(teams, 92621180)
