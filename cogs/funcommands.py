import discord
from discord.ext import commands
import random
import json

import sys
sys.path.append("../")
from data.facts import facts

class Fun_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        # quiz variables
        self.quiz_start = False
        self.question_number = 0
        self.points = 0
        self.questions = []
        self.current_question = {}

        with open("data//questions.json", "r") as f:
            self.data = json.load(f)

        self.data_size = len(self.data)
        self.first_q = 0;
    
    # fact command
    @commands.command(pass_context = True)
    async def fact(self, ctx):
        random_fact = random.choice(facts)
        fact_embed = discord.Embed(
            color = discord.Color.dark_red()
        )
        
        fact_embed.add_field(name = "Did you know?", value = random_fact)
        await ctx.send(embed = fact_embed)

    # quiz command
    @commands.command(pass_context = True)
    async def quiz(self, ctx, *arg):
        if(len(arg) == 0):
            await self.start_quiz(ctx)

        elif((len(arg) != 0) and (self.quiz_start == False)):
            error_embed = discord.Embed(
                colour = discord.Color.dark_red()
            )
            error_embed.add_field(name = "Invalid command!", value = "There is no quiz going on.\nUse the command `.quiz` to start a quiz!")
            await ctx.send(embed = error_embed)
            return

        elif(len(arg) > 1):
            await self.display_error_message(ctx)
            return

        else:
            if(arg[0].lower() == "quit"):
                await self.end_quiz(ctx)
            elif((arg[0].upper() == 'A') or (arg[0].upper() == 'B') or (arg[0].upper() == 'C')):
                await self.check_answer(ctx, arg[0].upper())
            else:
                await self.display_error_message(ctx)
                tryagain = discord.Embed(
                    colour = discord.Color.dark_red()
                )
                tryagain.set_author(name = "Try again!")

                await ctx.send(embed = tryagain)
                await self.display_question(ctx)
                return

    # QUIZ FUNCTIONS

    # Starts quiz 
    async def start_quiz(self, ctx):
        description = "- There are 5 questions and each question has 3 options (A, B and C)\n"
        description += "- To answer a question, use the command `.quiz <option>`\n"
        description += "- To quit, use the command `.quiz quit`"
        embed = discord.Embed(
            colour = discord.Color.dark_red(),
            title = "Quiz Instructions", 
            description = description
        )
        await ctx.send(embed = embed) 

        await self.reset_variables()
        self.quiz_start = True
 
        for i in range(5):
            (self.questions).append(self.data[(self.first_q + i) % self.data_size])
 
        self.current_question = self.questions[self.question_number]
        await self.display_question(ctx)
    
    # Displays the current question
    async def display_question(self, ctx):
        num = self.question_number + 1
        question = self.current_question['question']
        optionA = self.current_question['options'][0]
        optionB = self.current_question['options'][1]
        optionC = self.current_question['options'][2]
        embed = discord.Embed(
            colour = discord.Color.dark_red()
        )
        f1_logo = "https://i.ibb.co/QXL69Nq/logo.png"
        embed.set_author(name = f"Question {num}", icon_url = f1_logo)
        embed.add_field(name = question, value = f"{optionA}\n{optionB}\n{optionC}")
        await ctx.send(embed = embed)

        # Doesn't show this question in the next round because it's already been displayed
        self.first_q = (self.first_q + 1) % self.data_size

    # Displays the points scored at the end of the quiz
    async def display_points(self, ctx):
        embed = discord.Embed(
            colour = discord.Color.dark_red(),
            title = f"You have scored {self.points} / 5 "
        )
        f1_logo = "https://i.ibb.co/QXL69Nq/logo.png"

        embed.set_author(name = "Congratulations", icon_url = f1_logo)
        await ctx.send(embed = embed)
        await self.reset_variables()
    
    # Checks if the user's answer is correct
    async def check_answer(self, ctx, input):
        correct_answer = self.current_question['answer']
        embed = discord.Embed(
            colour = discord.Color.dark_red()
        )
        if(input == correct_answer):
            embed.set_author(name = "Correct Answer!")
            await ctx.reply(embed = embed)
            self.points += 1
        else:
            embed.add_field(name = "Incorrect Answer!", value = f"The correct answer was: {correct_answer}")
            await ctx.reply(embed = embed)

        await self.next_question(ctx)
        
    # Moves to the next question
    async def next_question(self, ctx):
        self.question_number += 1
        if(self.question_number == 5):
            await self.display_points(ctx)
            return
        else:
            self.current_question = self.questions[self.question_number]
            await self.display_question(ctx)
    
    # Ends the quiz and resets all quiz variables to default values
    async def end_quiz(self, ctx):
        embed = discord.Embed(
                    colour = discord.Color.dark_red()
        )
        embed.set_author(name = "Quiz Ended.")
        await ctx.send(embed = embed)
        await self.reset_variables()
        
    # Error message for invalid command during quiz
    async def display_error_message(self, ctx):
        error_embed = discord.Embed(
                colour = discord.Color.dark_red()
            )
        error_message = "The valid quiz commands are:\n"
        error_message += "- To start a quiz : `.quiz`\n"
        error_message += "- To answer a question: `.quiz <option>` (a, b or c)\n"
        error_message += "- To quit : `.quiz quit`"

        error_embed.add_field(name = "Invalid command!", value = error_message)
        await ctx.send(embed = error_embed)


    async def reset_variables(self):
        self.quiz_start = False
        self.question_number = 0
        self.points = 0
        self.questions = []
        self.current_question = {}
        

    
def setup(bot):
    bot.add_cog(Fun_Commands(bot))