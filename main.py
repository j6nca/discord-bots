import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print(f'Unloaded {extension}.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')





# @client.command()
# async def info(ctx, *args):
#     username = ' '.join(args)
#     print("Looking up information for ",username)
#     charData = retrieveChar(username)
#     info="""
#     **Character id**    %s
#     **Guild**           %s
#     **Faction**         %s
#     **Level**           %s
#     **Class**           %s
#     **Armor**           %s
#     **Helm**            %s
#     **Weapon**          %s
#     **Cape**            %s
#     **Pet**             %s
#     """ % (charData["ccid"],charData["guild"],charData["faction"],charData["level"],charData["class"],charData["armor"],charData["helm"],charData["weapon"],charData["cape"],charData["pet"])
#     embed = discord.Embed(
#         title=charData["username"]+"'s Info",
#         color=discord.Color.gold())
#     embed.add_field(name="\u200b", value=info)
#     await ctx.send(embed=embed)

# @client.command()
# async def epicgames(ctx, *args):
#     print("Checking Epic Games for new freebies...")
#     epicData = retrieveFreeGames()
#     embed = discord.Embed(
#         title="Free Games Week of " + str(date.today()),
#         color=discord.Color.purple())
#     await ctx.send(embed=embed)
#     #info we want to get: title, start/end dates, image, publisher, store url/app url, description, original price
#     for game in epicData['data']['Catalog']['searchStore']['elements']:
#         if game['price']['totalPrice']['originalPrice'] != 0:
#
#
#             embed = discord.Embed(
#                 title=game['title'],
#                 color=discord.Color.purple())
#             embed.add_field(name="Publishere", value=game['seller']['name'], inline= False)
#             embed.add_field(name="Original Price", value=game['price']['totalPrice']['fmtPrice']['originalPrice'], inline= False)
#             embed.add_field(name="Start", value=game['effectiveDate'])
#             #if lengths >1
#             if len(game['price']['lineOffers'])>=1:
#                 if len(game['price']['lineOffers'][0]['appliedRules']) >= 1:
#                     embed.add_field(name="End",
#                                     value=game['price']['lineOffers'][0]['appliedRules'][0]['endDate'])
#             if len(game['keyImages']) >= 1:
#                 embed.set_thumbnail(url=game['keyImages'][0]['url'])
#             await ctx.send(embed=embed)

# def scheduledMessages():
#     threading.Timer(1, scheduledMessages).start()
    
client.run(TOKEN)