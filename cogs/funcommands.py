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

        with open("data\questions.json", "r") as f:
            self.data = json.load(f)

        self.data_size = len(self.data)
        self.first_q = 0;
    
    # fact command
    @commands.command(pass_context = True)
    async def fact(self, ctx):
        random_fact = random.choice(facts)
        await ctx.send(f"```{random_fact}```")

    # quiz command
    @commands.command(pass_context = True)
    async def quiz(self, ctx, *arg):
        if(len(arg) == 0):
            await self.start_quiz(ctx)

        elif((len(arg) != 0) and (self.quiz_start == False)):
            error_message = "**Invalid command:** There is no quiz going on.\n"
            error_message += "    - Use the command *.quiz* to start a quiz!"
            await ctx.send(f'>>> {error_message}')
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
                await ctx.send("```Try Again!```")
                await self.display_question(ctx)
                return

    # QUIZ FUNCTIONS

    # Starts quiz 
    async def start_quiz(self, ctx):
        quiz_string = """ **Rules:**
        - There are 5 questions and each question has 3 options (A, B and C)
        - To answer with option A, use the command *.quiz A*
        - To quit, use the command *.quiz quit*
        """
        await ctx.send(f'>>> {quiz_string}') 
        await ctx.send("```Starting quiz..```")

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
        display_message = f"Question {num}: {question}\n{optionA}\n{optionB}\n{optionC}"
        await ctx.send(f"```{display_message}```")

        # Doesn't show this question in the next round because it's already been displayed
        self.first_q = (self.first_q + 1) % self.data_size

    # Displays the points scored at the end of the quiz
    async def display_points(self, ctx):
        message = f"```Congratulations! You have scored {self.points}/ 5```"
        await ctx.send(message)
        await self.end_quiz(ctx)
    
    # Checks if the user's answer is correct
    async def check_answer(self, ctx, input):
        correct_answer = self.current_question['answer']
        if(input == correct_answer):
            await ctx.reply("> **Correct Answer!**")
            self.points += 1
        else:
            await ctx.reply(f">>> **Incorrect Answer!**\nThe correct answer was **{correct_answer}**")

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
        await ctx.send(f'```Quiz ended.```')
        await self.reset_variables()
        
    # Error message for invalid command during quiz
    async def display_error_message(self, ctx):
        error_message = """**Invalid command.** The valid quiz commands are:
            - To start a quiz : *.quiz*
            - To answer a question: *.quiz A* *(or B or C)*
            - To quit : *.quiz quit*"""
        await ctx.send(f">>> {error_message}")

    async def reset_variables(self):
        self.quiz_start = False
        self.question_number = 0
        self.points = 0
        self.questions = []
        self.current_question = {}
        

    
def setup(bot):
    bot.add_cog(Fun_Commands(bot))