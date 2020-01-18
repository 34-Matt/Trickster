import discord
from discord.ext import commands
from random import choice

# About the bot
descript = 'Have you come to behold my brilliance. Very well, you have my permission.'

# Create bot
bot = commands.Bot(command_prefix='$',description=descript)

initial_extension = [
    'cogs.Japanese',
]

@bot.event
async def on_ready():
    # Runs when bot is running
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print("Loading Extensions")
    for ext in initial_extension:
        bot.load_extension(ext)

@bot.event
async def on_member_join(self,member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {}, come to over me your praise?'.format(member))

@bot.command()
@commands.guild_only()
async def info(ctx):
    # Creates an embed that discribes the bot
    embed = discord.Embed(title="Greetings",description=descript,color=0xf5e85d)
    
    embed.add_field(name="Name",value="Mayu")
    embed.add_field(name="Server count",value=f"{len(bot.guilds)}")
    embed.add_field(name="Invite",value="[Invite link](https://discordapp.com/oauth2/authorize?&client_id=347549865854763008&scope=bot&permissions=8)")

    await ctx.send(content=None,embed=embed)

@bot.command()
@commands.guild_only()
async def emote(ctx):
    # Sends a random, custom emote from the guild
    try:
        await ctx.send(choice(ctx.guild.emojis))
    except:
        await ctx.send("Looks like you don't have any custom emotes. This is unfit for someone of my stature.")

# Run bot
with open('token.txt','r') as f:
    lines = f.readlines()
    token = lines[0]

bot.run(token)