import discord
from discord.ext import commands
import asyncio
import json

mapFolder = "C:\\Users\\rhudson\\PycharmProjects\\mindustry_server_tools\\"

from discord.ext import commands

description = '''A simple discord bot using discord.py rewrite that lists the maps in maps.json. 
This lets players know what custom maps are currently loaded on the server'''

class MapsCog:
    def __init__(self, bot):
        self.bot = bot

    #when !maps is recieved run this:
    @commands.command(name='maps',aliases=['m','Maps','M'])
    async def Mlist(self,ctx):
        #Open the maps.json file
        with open(mapFolder + 'maps.json') as json_file:
            data = json.load(json_file)
            #Send the ['maps'] ['name'] to the discord channel
            print("maps command")
            await ctx.send("**Currently Loaded Maps:** \n" + "```" + "\n".join(x.get("name", "") for x in data["maps"]) + "```")


    @commands.command(name='showmap',aliases=['s','Showmap','S','ShowMap','show','Show'])
    async def showMap(self,ctx,map:str=None):
        if map is None:
            await ctx.send("Please specify a map.")
            return

        await ctx.send("Map: " + map, file=discord.File(map + '.png'))
        print('sending ' + mapFolder + map + '.png')

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(MapsCog(bot))
