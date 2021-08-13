import discord
from discord.ext import commands
from epicgames.fetchEpicStore import retrieveFreeGames
from datetime import date
from datetime import time
from datetime import datetime
import pytz



class Epic(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Bot Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded Epic Games Module.')

    # Bot Commands
    @commands.command()
    async def epicfree(self, ctx):
        print("Checking Epic Games for new freebies...")
        epicData = retrieveFreeGames()
        await ctx.send("Free Games Week of " + str(date.today()))
        # info we want to get: title, start/end dates, image, publisher, store url/app url, description, original price
        for game in epicData['data']['Catalog']['searchStore']['elements']:
            if game['price']['totalPrice']['originalPrice'] != 0 and game['promotions'] is not None:
                # offerStart = datetime.strptime(game['promotions']['promotionalOffers'][0]['promotionalOffers'][0]['startDate'], "%Y-%m-%dT%H:%M:%S.%fZ")
                now = False
                if (len(game['promotions']['promotionalOffers']) > 0):
                    now=True
                elif (len(game['promotions']['upcomingPromotionalOffers']) > 0):
                    now =False

                embed = discord.Embed(
                    title=("NOW" if now else "COMING SOON") + ": " + game['title'],
                    color=(discord.Color.purple() if now else discord.Color.gold()))
                embed.add_field(name="Publisher", value=game['seller']['name'], inline=False)
                embed.add_field(name="Original Price", value=game['price']['totalPrice']['fmtPrice']['originalPrice'],
                                inline=False)
                # embed.add_field(name=("Current Price" if now else "Future Price"), value='CA$0.00',
                #                 inline=False)

                est = pytz.timezone('US/Eastern')
                utc = pytz.utc
                fmt = '%Y-%m-%d %H:%M'

                gameDate = datetime.strptime(game['promotions'][('promotionalOffers' if now else 'upcomingPromotionalOffers')][0]['promotionalOffers'][0][('endDate' if now else 'startDate')], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=utc)
                embed.add_field(name=("Ends" if now else "Starts"), value=gameDate.astimezone(est).strftime(fmt) + " EST")
                for image in game['keyImages']:
                    if image['type'] == "OfferImageWide":
                        imageUrl = image['url']
                        embed.set_image(url=imageUrl)
                await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Epic(client))