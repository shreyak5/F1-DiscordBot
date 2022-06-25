import discord
from discord.ext import commands

class Help_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context = True, invoke_without_command = True)
    async def help(self, ctx):
        help_embed = discord.Embed(
            colour = discord.Color.dark_red()
        )
        
        f1_logo = "https://i.ibb.co/QXL69Nq/logo.png"

        help_embed.set_author(name = "Help Command", icon_url = f1_logo)
        help_embed.set_footer(text = "Type '.help <commandName>' for details on a command")
        help_embed.add_field(name = "General commands", value = "`.help`, `.hello`, `.bye`", inline = False)
        help_embed.add_field(name = "F1 commands", value = "`.drivers`, `.teams`, `.racewins`, `.news`", inline = False)
        help_embed.add_field(name = "Fun commands", value = "`.fact`, `.quiz`", inline = False)
        await ctx.send(embed = help_embed)

    # General commands
    @help.command(pass_context = True)
    async def hello(self, ctx):
        embed = discord.Embed(
            colour = discord.Color.dark_red()
        )
        f1_logo = "https://i.ibb.co/QXL69Nq/logo.png"

        embed.set_author(name = "Help Command: hello", icon_url = f1_logo)
        embed.add_field(name = "Description", value = "Says hello to the user.", inline = False)
        embed.add_field(name = "Syntax", value = "`.hello`", inline = False)
        await ctx.send(embed = embed)

    @help.command(pass_context = True)
    async def bye(self, ctx):
        embed = discord.Embed(
            colour = discord.Color.dark_red()
        )
        f1_logo = "https://i.ibb.co/QXL69Nq/logo.png"

        embed.set_author(name = "Help Command: bye", icon_url = f1_logo)
        embed.add_field(name = "Description", value = "Says bye to the user.", inline = False)
        embed.add_field(name = "Syntax", value = "`.bye`", inline = False)
        await ctx.send(embed = embed)

    # F1 commands
    @help.command(pass_context = True)
    async def drivers(self, ctx):
        embed = discord.Embed(
            colour = discord.Color.dark_red()
        )
        f1_logo = "https://i.ibb.co/QXL69Nq/logo.png"

        embed.set_author(name = "Help Command: drivers", icon_url = f1_logo)
        embed.add_field(name = "Description", value = "Displays the 2022 Driver Standings.", inline = False)
        embed.add_field(name = "Syntax", value = "`.drivers`", inline = False)
        await ctx.send(embed = embed)

    @help.command(pass_context = True)
    async def teams(self, ctx):
        embed = discord.Embed(
            colour = discord.Color.dark_red()
        )
        f1_logo = "https://i.ibb.co/QXL69Nq/logo.png"

        embed.set_author(name = "Help Command: teams", icon_url = f1_logo)
        embed.add_field(name = "Description", value = "Displays the 2022 Constructors/Teams Standings.", inline = False)
        embed.add_field(name = "Syntax", value = "`.teams`", inline = False)
        await ctx.send(embed = embed)

    @help.command(pass_context = True)
    async def racewins(self, ctx):
        embed = discord.Embed(
            colour = discord.Color.dark_red()
        )
        f1_logo = "https://i.ibb.co/QXL69Nq/logo.png"

        embed.set_author(name = "Help Command: racewins", icon_url = f1_logo)
        embed.add_field(name = "Description", value = "Displays the winners of all races this season.", inline = False)
        embed.add_field(name = "Syntax", value = "`.racewins`", inline = False)
        await ctx.send(embed = embed)

    @help.command(pass_context = True)
    async def news(self, ctx):
        embed = discord.Embed(
            colour = discord.Color.dark_red()
        )
        f1_logo = "https://i.ibb.co/QXL69Nq/logo.png"

        embed.set_author(name = "Help Command: news", icon_url = f1_logo)
        embed.add_field(name = "Description", value = "Gives you the latest F1 news.", inline = False)
        embed.add_field(name = "Syntax", value = "`.news`", inline = False)
        await ctx.send(embed = embed)

    # Fun commands
    @help.command(pass_context = True)
    async def fact(self, ctx):
        embed = discord.Embed(
            colour = discord.Color.dark_red()
        )
        f1_logo = "https://i.ibb.co/QXL69Nq/logo.png"

        embed.set_author(name = "Help Command: fact", icon_url = f1_logo)
        embed.add_field(name = "Description", value = "Gives you a random fact about Formula 1.", inline = False)
        embed.add_field(name = "Syntax", value = "`.fact`", inline = False)
        await ctx.send(embed = embed)

    @help.command(pass_context = True)
    async def quiz(self, ctx):
        embed = discord.Embed(
            colour = discord.Color.dark_red()
        )
        f1_logo = "https://i.ibb.co/QXL69Nq/logo.png"

        quiz_syntax = "To start a quiz: `.quiz`\n"
        quiz_syntax += "To end/quit an ongoing quiz: `.quiz quit`\n"
        quiz_syntax += "To answer a question: `.quiz <option>`"
        embed.set_author(name = "Help Command: quiz", icon_url = f1_logo)
        embed.add_field(name = "Description", value = "Lets you play a mini F1 themed quiz.", inline = False)
        embed.add_field(name = "Syntax", value = quiz_syntax, inline = False)
        await ctx.send(embed = embed)

    
def setup(bot):
    bot.add_cog(Help_Commands(bot))
