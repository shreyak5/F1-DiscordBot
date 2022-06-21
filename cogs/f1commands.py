import discord
from discord.ext import commands

import sys
sys.path.append("../")
from webscraping import standings

class F1_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("F1-Bot is ready!")

    #Commands
    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f'Hello {str(ctx.author).split("#")[0]}!')

    @commands.command()
    async def drivers(self, ctx):
        await ctx.send(f'```{standings.drivers_standings()}```')

    @commands.command()
    async def teams(self, ctx):
        await ctx.send(f'```{standings.team_standings()}```')

    @commands.command()
    async def raceresults(self, ctx):
        await ctx.send(f'```{standings.race_results()}```')
        
    
def setup(bot):
    bot.add_cog(F1_Commands(bot))