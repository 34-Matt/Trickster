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
            
    @commands.Cog.listener()
    async def on_message(self,ctx):
        # Check that message is not from self
        if ctx.author == self.bot.user:
            return
        if "this is the way" in ctx.content.lower():
            await ctx.channel.send("This is the way")

def setup(bot):
    bot.add_cog(Goddess(bot))