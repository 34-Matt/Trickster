import discord
from discord.ext import commands

class JapaneseCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    ### Romangi to Hiragana ###
    @commands.command()
    async def convertSingle(self,ctx):
        letter = ctx.message.content.split()[1]
        letNum = len(letter)
        output = 12352

        if letNum == 1:
            if letter == 'n':
                output += 83
            else:
                output += (2*self.vowalOffset(letter))
        elif letNum == 2:
            vowalOff = self.vowalOffset(letter[1])
            conOff,multi = self.conOffset(letter[0])

            # Deal with lower case 'tsu'
            if ((letter[0] == 't') or (letter[0] == 'd')) and (vowalOff > 2):
                output += 1
            # No 'yi' or 'yo'
            if (letter[0] == 'y') and (vowalOff == 3):
                vowalOff = 2
            elif (letter[0] == 'y') and (vowalOff == 5):
                vowalOff = 3
            # No 'wi'
            if (conOff == 't') and (vowalOff > 2):
                output -= 1
            
            # Get character
            output += conOff + (multi * vowalOff)

        await ctx.send(chr(output))


    def vowalOffset(self,vo):
        if vo == 'a':
            return 1
        elif vo == 'i':
            return 2
        elif vo == 'u':
            return 3
        elif vo == 'e':
            return 4
        elif vo == 'o':
            return 5
        else:
            return -1000

    def conOffset(self,con):
        if con == 'k':
            return 9,2
        elif con == 'g':
            return 10,2

        elif con == 's':
            return 19,2
        elif con == 'z':
            return 20,2

        elif con == 't':
            return 29,2
        elif con == 'd':
            return 30,2

        elif con =='n':
            return 41,1

        elif con == 'h':
            return 44,3
        elif con == 'b':
            return 45,3
        elif con == 'p':
            return 46,3

        elif con == 'm':
            return 61,1

        elif con == 'y':
            return 66,2

        elif con == 'r':
            return 72,1

        elif con == 'w':
            return 78,1


def setup(bot):
    bot.add_cog(JapaneseCog(bot))