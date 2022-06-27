import discord
from discord.ext import commands
import datetime
import random
import json

import sys
sys.path.append("../")
from webscraping import standings, news, upcoming

class F1_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        # news variables
        self.news_update_time = datetime.datetime.now() + datetime.timedelta(hours = 2)
        self.newslist = []

        # next race command variables
        self.nextrace_embed = None
        self.reset_date = datetime.date.today()

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
        self.news_update_time, self.newslist, message = await news.latest_news(ctx, self.news_update_time, self.newslist)
        
        if(len(self.newslist) == 0):
            embed = discord.Embed(
                colour = discord.Color.dark_red()
            )
            embed.set_author(name = "Failed to fetch data, try again :(")
            if(message == None):
                await ctx.send(embed = embed)
            else:
                await message.edit(content = "", embed = embed)
            return

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
        if(datetime.date.today() >= self.reset_date):
            self.nextrace_embed = None
        if(self.nextrace_embed == None):
            message = await ctx.send("```Fetching data...```")
            embed = await upcoming.next_race()
            self.nextrace_embed = embed
            if(embed == None):
                embed = discord.Embed(
                    colour = discord.Color.dark_red()
                )
                embed.set_author(name = "Failed to fetch data, try again :(")
            else:
                self.reset_date = datetime.date.today() + datetime.timedelta(days = 1)
            await message.edit(content = "", embed = embed)
        else:
            await ctx.send(embed = self.nextrace_embed)

    @commands.command(pass_context = True)
    async def schedule(self, ctx):
        embed = discord.Embed(
            colour = discord.Color.dark_red()
        )
        f1_logo = "https://i.ibb.co/QXL69Nq/logo.png"
        embed.set_author(name = "F1 2022 Upcoming Race Schedule", icon_url = f1_logo)

        display = []
        with open("data//schedule.json", "r") as f:
            display = json.load(f)
        
        current_day = datetime.date.today().day
        current_month = datetime.date.today().month
    
        months = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
        done = []
        for item in display:
            if(current_month > months[item["end-month"]]):
                done.append(item)
            elif(current_month == months[item["end-month"]]):
                if(current_day > int(item["end-date"])):
                    done.append(item)
                else:
                    break
            else:
                break
        
        for item in done:
            display.remove(item)
        
        for item in display:
            round = item["round"]
            name = item["title"] + " - " + item["place"]
            if(item["start-month"] == item["end-month"]):
                date = item["start-date"] + "-" + item["end-date"] + " " + item["start-month"]
            else:
                date = item["start-date"] + " " + item["start-month"]+ " - " + item["end-date"] + " " + item["end-month"]
            embed.add_field(name = round, value = f">>> {name}\n**{date}**", inline = False)

        await ctx.send(embed = embed)
    
def setup(bot):
    bot.add_cog(F1_Commands(bot))