import os


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
