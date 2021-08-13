import discord
from discord.ext import commands
from maplestory.charInfo import retrieveChar
from datetime import date
from datetime import time
from datetime import datetime
import pytz



class Maplestory(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Bot Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded Epic Games Module.')

    # Bot Commands
    @commands.command()
    async def msinfo(self, ctx, *args):
        username = ' '.join(args)
        allData = retrieveChar(username)
        overallData = allData[0]
        worldData = allData[1]

        info = """
            **Overall Rank**    %s
            **World**           %s
            **World Rank**      %s
            **Job**             %s
            **Level**           %s
            **Exp**             %s
            """ % (overallData["Rank"], overallData["WorldName"], worldData["Rank"], overallData["JobName"], overallData["Level"], overallData["Exp"])
        embed = discord.Embed(
            title=overallData["CharacterName"] + "'s Info",
            color=discord.Color.orange())
        embed.add_field(name="\u200b", value=info)
        embed.set_image(url=overallData["CharacterImgUrl"])
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Maplestory(client))