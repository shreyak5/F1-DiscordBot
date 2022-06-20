import discord
from discord.ext import commands

class F1_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("F1-Bot is ready!")

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f'Hello {str(ctx.author).split("#")[0]}!')

def setup(bot):
    bot.add_cog(F1_Commands(bot))