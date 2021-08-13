import requests
def retrieveChar(username: str):
    print(f'Looking up info for "{username}" on overall rankings')
    overallUrl = f'https://maplestory.nexon.net/api/ranking?id=overall&id2=legendary&rebootIndex=0&character_name={username}&page_index=1'
    overall = requests.get(overallUrl).json()

    print(f'Looking up info for "{username}" on {("reboot" if (overall[0]["WorldID"] == 45 ) else "non-reboot")} rankings')
    worldUrl = f'https://maplestory.nexon.net/api/ranking?id=overall&id2=legendary&rebootIndex={(1 if (overall[0]["WorldID"] == 45 ) else 2)}&character_name={username}&page_index=1'
    world = requests.get(worldUrl).json()
    return [overall[0], world[0]]


