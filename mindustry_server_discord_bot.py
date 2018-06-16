import discord
import json

from discord.ext import commands

description = '''A simple discord bot using discord.py that lists the maps in maps.json. 
This lets players know what custom maps are currently loaded on the server'''

#setup bot object and listen for !command
bot = commands.Bot(command_prefix='!', description=description)

#login stuff
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


#when !maps is recieved run this:
@bot.command()
async def maps():
    #Open the maps.json file
    with open('maps.json') as json_file:
        data = json.load(json_file)
        #Send the ['maps'] ['name'] to the discord channel
        await bot.say("**Currently Loaded Maps:** \n" + "```" + "\n".join(x.get("name", "") for x in data["maps"]) + "```")

#Runs the Bot
bot.run('Put your token here')