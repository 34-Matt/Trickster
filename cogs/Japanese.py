import discord
from discord.ext import commands
from cogs.JapaneseUtil import singleHiragana

class Japanese(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    ### Romangi to Hiragana ###
    @commands.command()
    async def Hiragana(self,ctx):
        letters = ctx.message.content.split()[1:]
        message = ""
        for letter in letters:
            message += singleHiragana(letter)
        await ctx.send(message)

def setup(bot):
    bot.add_cog(Japanese(bot))