import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
load_dotenv()

TOKEN = getenv('TOKEN')
bot = commands.Bot(command_prefix = ".", case_insensitive = True)

@bot.event
async def on_ready():
    print("F1-Bot is ready!")

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {str(ctx.author).split("#")[0]}!')
    
bot.run(TOKEN)