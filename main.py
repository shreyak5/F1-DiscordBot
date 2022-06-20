import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
load_dotenv()

TOKEN = getenv('TOKEN')
bot = commands.Bot(command_prefix = ".", case_insensitive = True)

#loading the cogs
for filename in os.listdir('./cogs'):
    bot.load_extension(f'cogs.{filename[:-3]}')
    
bot.run(TOKEN)