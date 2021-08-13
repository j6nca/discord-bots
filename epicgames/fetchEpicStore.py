import requests
def retrieveFreeGames():
    epicUrl = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=CA&allowCountries=CA"
    response = requests.get(epicUrl).json()
    return response
