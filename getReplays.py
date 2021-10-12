from codecs import decode, getreader
from collections import UserDict
import json
import urllib.parse
import urllib.request
import urllib3
import requests

def getReplayInfo(userName, server="generals.io", offset=0, numReplays=1):
    http = urllib3.PoolManager()
    replayLink = f"https://{server}/api/replaysForUsername?u={urllib.parse.quote_plus(userName)}&offset={offset}&count={numReplays}"
    infoObj = http.request("GET", f"{replayLink}")
    decodedInfo = infoObj.data.decode("utf-8")
    return json.loads(decodedInfo)

def writeReplayToFile(getReplayInfo):
    with open("replays.json", "a") as file:
        replayInf = getReplayInfo("sub",numReplays=1)
        file.write(json.dumps(replayInf, indent=4))
    return replayInf


#grabbing replay from us server
def getReplay(gameId):
    serverLink = "https://generalsio-replays-na.s3.amazonaws.com"
    replayLink = f"{serverLink}/{gameId}.gior"
    replay = requests.get(replayLink, allow_redirects=True)
    with open("replay.gior", "ab") as file:
        file.write(replay.content)
    return replayLink

subId = getReplayInfo("sub", offset=2)[0]["id"]
print(getReplay(subId))