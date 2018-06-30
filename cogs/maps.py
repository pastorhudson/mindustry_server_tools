import discord
from discord.ext import commands
import asyncio
import json
import datetime

'''
Set your map folder path including trailing slash.
On Windows use double \\ like c:\\users\\username\\mindustry\\mindustry-maps\\ 
On linux use normal full path like /home/username/mindustry/mindustry-maps/
Relative paths with ~/ don't seem to work.
'''
mapFolder = "<your_map_folder_path>"

from discord.ext import commands

description = '''A simple discord bot using discord.py rewrite that lists the maps in maps.json. 
This lets players know what custom maps are currently loaded on the server'''

class MapsCog:
    def __init__(self, bot):
        self.bot = bot

    #when !maps is recieved run this:
    @commands.command(name='maps',aliases=['m','Maps','M'])
    async def Mlist(self,ctx):
        print("------Maps Command Recieved--------")
        timeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        print(timeStamp)
        with open(mapFolder + 'maps.json') as json_file:
            data = json.load(json_file)
            await ctx.send("**Currently Loaded Maps:** \n" + "```" + "\n".join(x.get("name", "") for x in data["maps"]) + "```")
            print("**Currently Loaded Maps:** \n" + "```" + "\n".join(x.get("name", "") for x in data["maps"]) + "```")

    @commands.command(name='showmap',aliases=['Showmap','ShowMap','show','Show'])
    async def showMap(self,ctx,map:str=None):
        print("------Show Maps Command Recieved---")
        timeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        print(timeStamp)
        if map is None:
            await ctx.send("Please specify a map.")
            return

        await ctx.send("Map: " + map, file=discord.File(mapFolder + map + '.png'))
        print('sending ' + mapFolder + map + '.png')

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(MapsCog(bot))
