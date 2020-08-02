import discord
from discord.ext import commands
from forex_python.converter import CurrencyRates
from datetime import date

class Exchange(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

        self.exchangeNames = {
            "EUR":["eur","euro member countries"],
            "IDR":["idr","indonesia rupiah"],
            "BGN":["bgn","bulgaria lev"],
            "ILS":["ils","israel shekel"],
            "GBP":["gbp","united kingdom pound"],
            "DKK":["dkk","denmark krone"],
            "CAD":["cad","canada dollar"],
            "JPY":["jpy","japan yen"],
            "USD":["usd","united states dollar"]
        }
        self.CurrencyRates = CurrencyRates()

    @commands.command()
    async def ExchangeRate(self,ctx):
        ''' Gets exchange rate from between two currencies.

        $ExchangeRate USD to JPY => The exchange rate from USD to JPY is xxx.xx
        '''

        letters = ctx.message.content.split(maxsplit=1)[1]
        letters = letters.lower()
        letters = letters.split("to")

        fromAddress = letters[0].strip()
        toAddress = letters[1].strip()
        fromID = self.getAddressName(fromAddress)
        toID = self.getAddressName(toAddress)
        print(letters)

        if fromID == -1:
            await ctx.send("Was unable to find currency for {}".format(fromAddress))
        elif toID == -1:
            await ctx.send("Was unable to find currency for {}".format(toAddress))
        else:
            rate = self.CurrencyRates.get_rate(fromID,toID)
            await ctx.send("The exchange rate from {} to {} is {}".format(fromID,toID,rate))

    def getAddressName(self,address):
        '''Gets the proper address name for desired currency

        address is the name of the desired currency

        returns the id of the desired currency or -1 if none are valid
        '''
        for id,addArray in self.exchangeNames.items():
            if address in addArray:
                return id

        return -1


def setup(bot):
    bot.add_cog(Exchange(bot))
