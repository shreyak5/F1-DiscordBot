import discord
from discord.ext import commands

import sys
sys.path.append("../")
from webscraping import standings

class F1_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Commands
    @commands.command(pass_context = True)
    async def drivers(self, ctx):
        await ctx.send(f'```{standings.drivers_standings()}```')

    @commands.command(pass_context = True)
    async def teams(self, ctx):
        await ctx.send(f'```{standings.team_standings()}```')

    @commands.command(pass_context = True)
    async def racewins(self, ctx):
        await ctx.send(f'```{standings.race_wins()}```')
      
def setup(bot):
    bot.add_cog(F1_Commands(bot))