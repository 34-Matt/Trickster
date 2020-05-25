import discord
from discord.ext import commands
from cogs.gambleUtil import *

#import cv2
from PIL import Image
import numpy as np
import io

class gamble(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.paper = np.asarray(Image.open("Images/Red_Sword.png"))
        self.rock = np.asarray(Image.open("Images/Green_Axe.png"))
        self.scissor = np.asarray(Image.open("Images/Blue_Lance.png"))

    @commands.command()
    async def roshambo(self,ctx):
        ''' Plays a game of rock-paper-scissors with the person
        '''

        # Get response from human
        person = ctx.message.content.split()[1].lower()
        person = rpsConvertHumanChoice(person)
        if person == 0:
            await ctx.send("Not a valid choice, not worth my time.")
            return

        # Get response for bot
        machine,cheat = rpsGetMachineChoice(person)

        # Determine winner
        if cheat == 1:
            result = "You did not stand a chance against my powers."
            rTitle = "You Lose"
        elif cheat == -1:
            result = "There, you finally won. Hope your happy, you totally deserved it."
            rTitle = "You Win"
        else:
            winner = rpsGetWinner(person,machine)
            if winner == 0:
                result = "Looks like a draw. Want to try again?"
                rTitle = "Tie"
            elif winner == 1:
                result = "Looks like you won, well played."
                rTitle = "You Win"
            else:
                result = "Looks like I won fair and square."
                rTitle = "You Lose"

        # Send Result
        hString,hImage = self.rpsName(person)
        mString,mImage = self.rpsName(machine)
        #img = cv2.hconcat([hImage,mImage])
        img = Image.fromarray(np.hstack((hImage,mImage)))
        arr = io.BytesIO()
        img.save(arr,format="PNG")
        arr.seek(0)
        file = discord.File(arr,filename="rpsResult.png")

        embed = discord.Embed(title="Rock-Paper-Scissors",
            description="A game of ~~luck~~ wits between two opponents.",
            color=0xf5e85d)
        embed.set_thumbnail(url="attachment://rpsResult.png")
        embed.add_field(name=rTitle,value = result,inline=False)
        embed.add_field(name="Your Choice",value=hString,inline=True)
        embed.add_field(name="My Choice",value=mString,inline=True)
        await ctx.send(file=file,embed=embed)
        
    def rpsName(self,choice):
        if choice == 1:
            return "Rock",self.rock
        elif choice == 2:
            return "Paper",self.paper
        elif choice == 3:
            return "Scissors",self.scissor
        else:
            return "Invalid"

def setup(bot):
    bot.add_cog(gamble(bot))
