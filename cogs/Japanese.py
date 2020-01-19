import discord
from discord.ext import commands
from cogs.JapaneseUtil import singleChar

class Japanese(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def Hiragana(self,ctx):
        ''' Convert text to Hiragana. Need to manually add spaces in the romanji characters.

        $Hiragana ko n ba wa => こんばわ
        '''

        letters = ctx.message.content.split()[1:]
        message = ""
        for letter in letters:
            message += singleChar(letter.lower(),False)
        await ctx.send(message)

    @commands.command()
    async def Katakana(self,ctx):
        ''' Convert text to Katakana. Need to manually add spaces in the romanji characters.

        $Katakana ko n ba wa => コンバワ
        '''
        
        letters = ctx.message.content.split()[1:]
        message = ""
        for letter in letters:
            message += singleChar(letter.lower(),True)
        await ctx.send(message)

def setup(bot):
    bot.add_cog(Japanese(bot))