import re
import requests

#BADGES - https://account.aq.com/CharPage/Badges?ccid=
#INVENTORY - https://account.aq.com/CharPage/Inventory?ccid=

def retrieveChar(username: str):
    charUrl = "https://account.aq.com/CharPage?id="+username
    response = requests.get(charUrl)
    ccidReg = re.compile(r'var ccid = ((?:(?!;).)*)')
    usernameReg = re.compile(r'h1>((?:(?!<).)*)')

    lvlReg = re.compile(r'Level:</label> ((?:(?!<).)*)')
    classReg = re.compile(r'Class:</label> ((?:(?!<).)*)')
    helmReg = re.compile(r'Helm:</label> ((?:(?!<).)*)')
    armorReg = re.compile(r'Armor:</label> ((?:(?!<).)*)')
    wepReg = re.compile(r'Weapon:</label> ((?:(?!<).)*)')
    capeReg = re.compile(r'Cape:</label> ((?:(?!<).)*)')
    petReg = re.compile(r'Pet:</label> ((?:(?!<).)*)')
    guildReg = re.compile(r'Guild:</label> ((?:(?!<).)*)')
    factionReg = re.compile(r'Faction:</label> ((?:(?!<).)*)')

    charData = {
        "username": usernameReg.findall(response.text)[0],
        "ccid": ccidReg.findall(response.text)[0],
        "guild": guildReg.findall(response.text)[0],
        "level": lvlReg.findall(response.text)[0],
        "class": classReg.findall(response.text)[0],
        "armor": armorReg.findall(response.text)[0],
        "weapon": wepReg.findall(response.text)[0],
        "helm": helmReg.findall(response.text)[0],
        "cape": capeReg.findall(response.text)[0],
        "pet": petReg.findall(response.text)[0],
        "faction": factionReg.findall(response.text)[0]
    }
    #No empty string equips
    for key in charData:
        if charData[key]=="":
            charData[key] == "None"

    return charData
