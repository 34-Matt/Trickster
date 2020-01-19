import discord
from discord.ext import commands

class Goddess(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {}, come to over me your praise?'.format(member))

def setup(bot):
    bot.add_cog(Goddess(bot))