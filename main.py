import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from aqw.charInfo import retrieveChar

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# client = discord.Client()
client = commands.Bot(command_prefix=".")
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def info(ctx, *args):
    username = ' '.join(args)
    print("Looking up information for ",username)
    charData = retrieveChar(username)
    info="""
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
    """ % (charData["ccid"],charData["guild"],charData["faction"],charData["level"],charData["class"],charData["armor"],charData["helm"],charData["weapon"],charData["cape"],charData["pet"])
    embed = discord.Embed(
        color=discord.Color.gold())
    embed.add_field(name=charData["username"]+"'s Info", value=info)
    # embed.add_field(name="Id", value=charData["ccid"] if charData["ccid"] != '' else "None", inline=False)
    # # embed.add_field(name='\u200b', value='\u200b', inline=True)
    #
    # embed.add_field(name="Guild", value=charData["guild"] if charData["guild"] != '' else "None", inline=True)
    # embed.add_field(name="Faction", value=charData["faction"] if charData["faction"] != '' else "None", inline=True)
    # embed.add_field(name="Level", value=charData["level"] if charData["level"] != '' else "None", inline=True)
    #
    # embed.add_field(name="Class", value=charData["class"] if charData["class"] != '' else "None", inline=True)
    # embed.add_field(name="Armor", value=charData["armor"] if charData["armor"] != '' else "None", inline=True)
    # embed.add_field(name="Helm", value=charData["helm"] if charData["helm"] != '' else "None", inline=True)
    # embed.add_field(name="Weapon", value=charData["weapon"] if charData["weapon"] != '' else "None", inline=True)
    # embed.add_field(name="Cape", value=charData["cape"] if charData["cape"] !='' else "None", inline=True)
    # embed.add_field(name="Pet", value=charData["pet"] if charData["pet"] != '' else "None", inline=True)
    await ctx.send(embed=embed)

client.run(TOKEN)