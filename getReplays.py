import urllib.parse

def getReplayURL(userName, server="generals.io", offset=0, numReplays=1):
    return f"https://{server}/api/replaysForUsername?u={urllib.parse.quote_plus(userName)}&offset={offset}&count={numReplays}"

a = getReplayURL("sub")

print(a)