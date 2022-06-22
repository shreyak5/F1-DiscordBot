import discord
from discord.ext import commands
import random

import sys
sys.path.append("../")
from data.facts import facts

class Fun_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fact(self, ctx):
        random_fact = random.choice(facts)
        await ctx.send(f"```{random_fact}```")

    @commands.command()
    async def quiz(self, ctx):
        await ctx.send(f'> Starting quiz!')  

    
def setup(bot):
    bot.add_cog(Fun_Commands(bot))