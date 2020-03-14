import discord
from discord.ext import commands
from cogs.gambleUtil import *

import cv2

class gamble(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.rock = cv2.imread("Images/Red_Sword.png")
        self.paper = cv2.imread("Images/Green_Axe.png")
        self.scissor = cv2.imread("Images/Blue_Lance.png")

    @commands.command()
    async def rockpaperscissors(self,ctx):
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
            result = "You did not stand with my powers."
        elif cheat == -1:
            result = "There, you finally won. Hope your happy, you totally deserved it."
        else:
            winner = rpsGetWinner(human,machine)
            if winner == 0:
                result = "Looks like a draw. Want to try again?"
            elif winner == 1:
                result = "Looks like you won, well played."
            else:
                result = "Looks like I won fair and square."

        # Send Result
        hString,hImage = rpsName(human)
        mString,mImage = rpsName(machine)

        embed = discord.Embed(title="Rock-Paper-Scissors",
            description="A game of ~~luck~~ wits between two opponents.",
            color=0xf5e85d)
        img = cv2.hconcat([hImage,mImage])
        embed.setImage(img)
        embed.add_field(name=None,value = result)
        embed.add_field(name="Your Choise",value=hString)
        embed.add_field(name="My Choise",value=mString,inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(gamble(bot))
