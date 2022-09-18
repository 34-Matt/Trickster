import discord
from discord.ext import commands
from util.chessUtil import *

class Chess(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @updateChessDatabase
    async def register(self, ctx, chessName):
        '''Registers you to the specified account on chess.com
        
        chessName: the name of the account on chess.com
        '''
        CHESSDATABASE[ctx.author.name] = chessName
    
    @commands.command()
    async def player_info(self, ctx, *args):
        '''Extracts player information from chess.com
        
        If name provided, will look for that user. Otherwise, will search for your username.
        '''
        if len(args) > 1:
            user = discord2chess(args[1])
        else:
            user = discord2chess(ctx.author.name)
        
        try:
            embed = displayPlayer(user, False)
            await ctx.send(embed=embed)
        except Exception as e:
            print("Failed to find player ", user)
            print(e, '\n')
            await ctx.send("Failed to find player {}".format(user))
    
    @commands.command()
    async def compare_player(self, ctx, opponent):
        '''Compares your odds of winning against an opponent.
        
        opponent: the discord or Chess.com name of the person to compare against.
        '''
        player = discord2chess(ctx.author.name)
        opponent = discord2chess(opponent)
        _, embed = comparePlayers(player, opponent)
        ctx.send(embed=embed)
        
            

def setup(bot):
    bot.add_cog(Chess(bot))