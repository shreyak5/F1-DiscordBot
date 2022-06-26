import discord
from discord.ext import commands
import datetime
import random

import sys
sys.path.append("../")
from webscraping import standings, news, upcoming

class F1_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        # news variables
        self.update_hour = (datetime.datetime.now().hour + 2) % 24
        self.newslist = []

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

    @commands.command(pass_context = True)
    async def news(self, ctx):
        self.update_hour, self.newslist, message = await news.latest_news(ctx, self.update_hour, self.newslist)
        # make this random
        article = random.choice(self.newslist)
        self.newslist.remove(article)

        news_embed = discord.Embed(
            color = discord.Color.dark_red()
        )

        f1_logo = "https://i.ibb.co/QXL69Nq/logo.png"
        news_embed.set_author(name = "Latest F1 news", icon_url = f1_logo)
        news_embed.add_field(name = article["headline"], value = f'Read more:\n{article["link"]}')

        if(message == None):
            await ctx.send(embed = news_embed)
        else:
            await message.edit(content = "", embed = news_embed)

    @commands.command(pass_context = True)
    async def nextrace(self, ctx):
        message = await ctx.send("```Fetching data...```")
        await message.edit(content = "", embed = await upcoming.next_race())
    
def setup(bot):
    bot.add_cog(F1_Commands(bot))