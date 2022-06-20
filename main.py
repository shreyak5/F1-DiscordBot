import discord
from discord.ext import commands

TOKEN = "OTg4MzkyOTYzNDM0NTA4MzE4.GABQuY.9dZ6BnlH64uOJ6DJ1t_k9i6Izy5qzN9CLRvyYg"

bot = commands.Bot(command_prefix = ".", case_insensitive = True)

@bot.event
async def on_ready():
    print("F1-Bot is ready!")

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {str(ctx.author).split("#")[0]}!')
    
bot.run(TOKEN)