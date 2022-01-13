import requests
from riotwatcher import LolWatcher
import base64

def get_SummonerName(summonerId):
    watcher = LolWatcher('RGAPI-93e0f3c9-354b-47b1-9140-2ca8cbff70f2')
    s = watcher.summoner.by_id("EUW1", summonerId)
    print(s)

if __name__ == '__main__':
    watcher = LolWatcher('RGAPI-93e0f3c9-354b-47b1-9140-2ca8cbff70f2')
    summoner = watcher.summoner.by_name("EUW1", 'DCPentan')
    key = 'RGAPI-93e0f3c9-354b-47b1-9140-2ca8cbff70f2'
    summonerid = '92621180'
    enc = summonerid.encode('ascii')
    b64enc = base64.b64encode(enc)
    print(get_SummonerName('U3F94pkpR3WpTY6RuSMo1Od1KcB2LUay-iZtrt99v2WEG1c'))