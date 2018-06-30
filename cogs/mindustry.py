import discord
from discord.ext import commands
import asyncio
import websockets
import base64
import json
import datetime

class MindustryCog:
    def __init__(self, bot):
        self.bot = bot

    #LengthOfHostName HostName, LengthOfMapName MapName, PlayerAmount, Wave, Version
    @commands.command(name='ping',aliases=['p','Ping','P'])
    async def Mping(self,ctx,server:str='None'):
        print("------Ping Command Recieved--------")
        if server is 'None':
            await ctx.send("Please specify a server.")
            return
        print("Pinging " + server)
        async with websockets.connect(f'ws://{server}:6568') as websocket:
            await websocket.send('ping')
            reply = await asyncio.wait_for(websocket.recv(),timeout=1)
            dreply = base64.b64decode(reply)
            embed = discord.Embed(title=server,
                                  colour=0x33CCFF)

            embed.add_field(name='Host',
                            value=str(dreply[1:(dreply[0]+1)])[2:(dreply[0]+2)])
            embed.add_field(name='Map',
                            value=str(dreply[(dreply[0]+2):(dreply[0]+2+dreply[dreply[0]+1])])[2:(dreply[0]+dreply[dreply[0]])])
            embed.add_field(name='Players',
                            value=dreply[dreply[0]+5+dreply[dreply[0]+1]])

            await ctx.send(embed=embed)

            try:
                timeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
                print(timeStamp)
                with open('servers.json') as json_file:
                    jservers = json.load(json_file)
            except FileNotFoundError:
                print("No servers.json found. One will be created.")
                jservers = {1: {"lastSuccess": timeStamp, "host": "mindustry.us.to", "failCount": 0},
                            2: {"lastSuccess": timeStamp, "host": "mindustry.pastorhudson.com", "failCount": 0}}
            finally:
                jserv = {"lastSuccess": timeStamp, "host": server, "failCount": 0}

                try:
                        lastKey = 0
                        newServer = False
                        for key, value in jservers.items():
                            if lastKey < int(key):
                                lastKey = int(key)
                            if jserv['host'] in value['host']:
                                print(jserv['host'] + " is already in the list.")
                                newServer = False
                                break
                            else:
                                newServer = True
                except Exception as e:
                    print(type(e))
                finally:
                    if newServer is True:
                        print("Adding new server: " + jserv['host'])
                        jservers[str(lastKey+1)] = jserv
                        with open('servers.json', 'w') as outfile:
                            json.dump(jservers, outfile, indent=4)


# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(MindustryCog(bot))
