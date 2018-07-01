import discord
from discord.ext import commands
import asyncio
import json
import datetime
import os
import glob
import refreshmaps
import io
import aiohttp

'''
Set your map folder path including trailing slash.
On Windows use double \\ like c:\\users\\username\\mindustry\\mindustry-maps\\ 
On linux use normal full path like /home/username/mindustry/mindustry-maps/
Relative paths with ~/ don't seem to work.
'''
#mapFolder = "<your map folder here.>"
mapFolder = ""

from discord.ext import commands

description = '''A simple discord bot using discord.py rewrite that lists the maps in maps.json. 
This lets players know what custom maps are currently loaded on the server'''


class MapsCog:
    def __init__(self, bot):
        self.bot = bot


    #when !maps is recieved run this:
    @commands.group(name='maps',aliases=['m','Maps','M','map','Map'])
    async def maps(self,ctx):
        if ctx.invoked_subcommand is None:
            print("------Maps Command Recieved--------")
            timeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
            print(timeStamp)
            with open(mapFolder + 'maps.json') as json_file:
                data = json.load(json_file)
            await ctx.send(
                "**Currently Loaded Maps:** \n" + "```" + "\n".join(
                    x.get("name", "") for x in data["maps"]) + "```")
            print("**Currently Loaded Maps:** \n" + "```" + "\n".join(
                x.get("name", "") for x in data["maps"]) + "```")


    @maps.command(name='showmap',aliases=['Showmap','ShowMap','show','Show'])
    async def showMap(self,ctx,map:str=None):
        print("------Show Maps Command Recieved---")
        timeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        print(timeStamp)
        if map is None:
            await ctx.send("Please specify a map.")
            return

        await ctx.send("Map: " + map, file=discord.File(mapFolder + map + '.png'))
        print('sending ' + mapFolder + map + '.png')

    @maps.command(name='load', aliases=['Load', 'l', 'L', '-load'],pass_context=True)
    async def loadMap(self,ctx):
        print("------Load Map Command Recieved---")
        alreadyGotFile = False
        timeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        print(timeStamp)
        if "http" in ctx.message.content:
            print("This looks like a url to me!")
            url = ctx.message.content[ctx.message.content.find('http'):]
            print(str(ctx.message.author) + " wants us to get " + url)
            fileName = (ctx.message.content[ctx.message.content.rfind('/')+1:])
            if url.endswith('.png'):
                dirMaps = ([os.path.basename(x) for x in glob.glob(mapFolder + '*.png')])
                if fileName.lower() not in dirMaps:
                  async with aiohttp.ClientSession() as session:
                    async with session.get(url) as resp:
                        if resp.status != 200:
                            return await ctx.send('Could not download file...')

                        with open(fileName, 'wb') as fd:
                            while True:
                                chunk = await resp.content.read(512*1024)
                                if not chunk:
                                    break
                                fd.write(chunk)
                            #fd.close()
                            alreadyGotFile = True
                            print(fileName + " saved!")
                            await ctx.send(fileName.lower() + " loaded to the server.")
                            refreshmaps.refresh_maps()
                else:
                    print(str(
                        ctx.message.author) + " tried to send " + fileName + ", but it's already on the server.")
                    await ctx.send(
                        fileName + " is already on the server. Use !maps to see the loaded maps.")
                    alreadyGotFile = True
        if not alreadyGotFile:
            try:
                attachment = ctx.message.attachments[0]
            except IndexError:
                print("Error: file not attached.")
                await ctx.send("Please attach a .png map file")
                return
            if attachment.filename.endswith('.png'):
                dirMaps = ([os.path.basename(x) for x in glob.glob(mapFolder + '*.png')])
                if attachment.filename.lower() not in dirMaps:
                    await attachment.save(mapFolder + attachment.filename)
                    print(str(ctx.message.author) + " loaded " + attachment.filename)
                    refreshmaps.refresh_maps()
                else:
                    print(str(ctx.message.author) + " tried to send " + attachment.filename+", but it's already on the server.")
                    await ctx.send(attachment.filename + " is already on the server. User !maps to see the loaded maps.")


            else:
                print(str(ctx.message.author) + " tried to send " + attachment.filename)
                await ctx.send("Please attach a .png map file")

    @maps.command(name='refresh', aliases=['Refresh'], pass_context=True)
    async def refreshMaps(self, ctx):
        print('Refresh Maps!')
        refreshmaps.refresh_maps()
        await ctx.send("Server maps refreshed.")



    @commands.command(name='showmap', aliases=['Showmap', 'ShowMap', 'show', 'Show'])
    async def showMap(self, ctx, map: str = None):
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
