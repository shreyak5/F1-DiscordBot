import discord
from discord.ext import commands
import os

class General_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        os.systen("pyppeteer-install")
        print("F1-Bot is ready!")

    #Commands
    @commands.command(pass_context = True)
    async def hello(self, ctx):
        await ctx.send(f'Hello {str(ctx.author).split("#")[0]}!')

    @commands.command(pass_context = True)
    async def bye(self, ctx):
        await ctx.send(f'Byebye {str(ctx.author).split("#")[0]}!')


def setup(bot):
    bot.add_cog(General_Commands(bot))