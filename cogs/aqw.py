import discord
from discord.ext import commands
from aqw.charInfo import retrieveChar


class Aqw(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Bot Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Loaded Adventure Quest Worlds Module.')

    # Bot Commands
    @commands.command()
    async def aqwinfo(self, ctx, *args):
        username = ' '.join(args)
        print("Looking up information for \"", username,"\"")
        charData = retrieveChar(username)
        info = """
            **Character id**    %s
            **Guild**           %s
            **Faction**         %s
            **Level**           %s
            **Class**           %s
            **Armor**           %s
            **Helm**            %s
            **Weapon**          %s
            **Cape**            %s
            **Pet**             %s
            """ % (charData["ccid"], charData["guild"], charData["faction"], charData["level"], charData["class"],
                   charData["armor"], charData["helm"], charData["weapon"], charData["cape"], charData["pet"])
        embed = discord.Embed(
            url="https://account.aq.com/CharPage?id="+ username,
            title=charData["username"] + "'s Info",
            color=discord.Color.gold())
        embed.add_field(name="\u200b", value=info)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Aqw(client))