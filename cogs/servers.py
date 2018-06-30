import discord
from discord.ext import commands
import asyncio
import websockets
import base64
import datetime
import json
import subprocess
import re
import async_timeout
from socket import gaierror

class MindustryCog:
    def __init__(self, bot):
        self.bot = bot

    #LengthOfHostName HostName, LengthOfMapName MapName, PlayerAmount, Wave, Version
    @commands.command(name='servers',aliases=['s','Servers','S'])
    async def Servers(self,ctx,server:str='mindustry.pastorhudson.com'):
        await ctx.send("Pinging Servers. This could take a bit. . .")
        timeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        try:
            print("------Server command received------")
            print(timeStamp)
            with open('servers.json') as json_file:
                jservers = json.load(json_file)

        except:
            jservers = {1:{"lastSuccess":timeStamp, "host": "mindustry.us.to", "failCount":0},2:{"lastSuccess":timeStamp, "host": "mindustry.pastorhudson.com", "failCount":0}}
            print('servers.json not found. One will be created.')

        #for x in goodHosts:
        finally:
            serverList = []
            for key, jserv in jservers.items():
                try:
                    async with websockets.connect(f'ws://{jserv["host"]}:6568') as websocket:
                        await websocket.send('ping')
                        reply = await asyncio.wait_for(websocket.recv(),timeout=1)
                        dreply = base64.b64decode(reply)
                        jserv['failCount'] = 0
                        jserv['lastSuccess'] = timeStamp
                        players ="**"+str(dreply[dreply[0] + 5 + dreply[dreply[0] + 1]])+"** players "
                        currentMap = "on map **'" + str(dreply[(dreply[0]+2):(dreply[0]+2+dreply[dreply[0]+1])])[2:(dreply[0]+dreply[dreply[0]+1])]+"**"
                        wave = "wave **" + str(dreply[dreply[0]+5+dreply[dreply[0]+1]+4])+"**"
                        print(" ".join(["**" + jserv['host'] + " /**",players,currentMap,wave]))
                        serverList.append(" ".join(["**" + jserv['host'] + " /**",players,currentMap,wave]))
                except Exception as e:
                    print(type(e))
                    print(e)
                    jserv['failCount'] += 1

            embed = discord.Embed(title="**Server List**", colour=discord.Colour(0x85ff),
                                              url="https://github.com/pastorhudson/mindustry_server_tools",
                                              description="\n".join(serverList))
        await ctx.send(embed=embed)
        print("\n".join(serverList))
        with open('servers.json', 'w') as outfile:
            json.dump(jservers, outfile, indent=4)


# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(MindustryCog(bot))
