import discord
from discord.ext import commands
import pickle
import random
import asyncio

'''
Initialisation
'''

class HelpCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='info')
    async def info(self, ctx):
        embed = discord.Embed(title='Bot info',
                              description="This is a mindustry server bot.",
                              colour=0x008800)
        embed.set_author(name=self.bot.user.name,
                         icon_url=self.bot.user.avatar_url_as(format='png'))
        embed.add_field(name='Hello!',
                        value='I am a bot originally created by Greenfoot5 and extended by pastorhudson.')
        embed.add_field(name='Prefix',
                        value='My current prefix is `!`')
        embed.add_field(name='It broke what do I do?',
                        value='Post in on the support server and wait for it to be notied. Until then, please be patient. If possible warn others of the problem.')
        embed.add_field(name='Can I support the bot in any way?',
                        value="Other than joining the support server and offering input not at the moment.")
        embed.set_footer(text=ctx.guild.name,
                         icon_url=ctx.guild.icon_url_as(format='png'))

        await ctx.send(content='**Displaying info**', embed=embed)

        
    @commands.group(name='help',aliases=['h','Help','H'])
    async def helps(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title='Help',
                              description=f"Type `!help <category>` for more info on a category.\n[] Are optional.\n<> Are required.\n() Are aliases",
                              colour=0x469BFF)

            embed.add_field(name='Aliases',
                            value='`Help`,`help`,`H`,`h')
            embed.add_field(name="24/7 Mindustry Server",
                            value="[mindustry.pastorhudson.com]")
            embed.add_field(name='ping [server]',
                            value="Pings a mindustry server. Defaults to [mindustry.pastorhudson.com] if no server given")
            embed.add_field(name='map',
                            value="Lists maps currently loaded on [mindustry.pastorhudson.com]")
            embed.add_field(name='map load <attach .png>',
                            value="Upload a map .png file to [mindustry.pastorhudson.com]")
            embed.add_field(name='map refresh',
                            value="Rebuild the map list on [mindustry.pastorhudson.com]")
            embed.add_field(name='showmap <map_name>',
                            value="Shows the requested map")
            embed.add_field(name='servers',
                            value="Shows a list of currently running servers")
            embed.add_field(name='ping <hostname>',
                            value="Shows status of server, and adds it to the !servers list")

        await ctx.send(content='**Displaying help**', embed=embed)



def setup(bot):
    bot.add_cog(HelpCog(bot))
