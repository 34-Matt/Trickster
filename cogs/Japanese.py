import discord
from discord.ext import commands
from cogs.JapaneseUtil import singleChar

class Japanese(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def Hiragana(self,ctx):
        ''' Convert text to Hiragana.

        $Hiragana konbawa => こんばわ
        '''

        letters = ctx.message.content.split(maxsplit=1)[1]
        letters = letters.lower()
        letters = breakJapaneseWord(letters)
        message = ""
        for letter in letters:
            message += singleChar(letter,False)
        await ctx.send(message)

    @commands.command()
    async def Katakana(self,ctx):
        ''' Convert text to Katakana.

        $Katakana konbawa => コンバワ
        '''

        letters = ctx.message.content.split(maxsplit=1)[1]
        letters = letters.lower()
        letters = breakJapaneseWord(letters)
        message = ""
        for letter in letters:
            message += singleChar(letter,True)
        await ctx.send(message)

def setup(bot):
    bot.add_cog(Japanese(bot))
