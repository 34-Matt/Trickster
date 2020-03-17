import discord
from discord.ext import commands
from random import choice

# About the bot
descript = 'Have you come to behold my brilliance. Very well, you have my permission.'

# Create bot
bot = commands.Bot(command_prefix='$',description=descript)

initial_extension = [ # Add new cogs here
    'cogs.Japanese',
    "cogs.Goddess",
    "cogs.gamble",
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
        print("Loaded {}".format(ext))
    await bot.change_presence(activity=discord.Game("Awaiting my subjects"))
    print("Bot is ready for use")

@bot.command()
@commands.guild_only()
async def info(ctx):
    # Creates an embed that discribes the bot
    embed = discord.Embed(title="Greetings",description=descript,color=0xf5e85d)
    
    embed.add_field(name="Name",value="Mayu")
    embed.add_field(name="Server count",value=f"{len(bot.guilds)}")
    embed.add_field(name="Invite",value="[Invite link](https://discordapp.com/oauth2/authorize?&client_id=347549865854763008&scope=bot&permissions=8)")
    embed.add_field(name="Github",value="[Github link](https://github.com/34-Matt/Trickster)")

    await ctx.send(content=None,embed=embed)

@bot.command()
@commands.guild_only()
async def emote(ctx):
    # Sends a random, custom emote from the guild
    try:
        await ctx.send(choice(ctx.guild.emojis))
    except:
        await ctx.send("Looks like you don't have any custom emotes. This is unfit for someone of my stature.")

@bot.command()
async def load(ctx):
    extension = ctx.message.content.split()[1]
    try:
        bot.load_extension("cogs."+extension)
        print("Loaded {}".format(extension))
        await ctx.send("Your prayers have been answered.")
    except Exception as error:
        print("{} cannot be loaded. [{}]".format(extension,error))
        await ctx.send("Build me a temple, then I shall perform your task.")

@bot.command()
async def unload(ctx):
    extension = ctx.message.content.split()[1]
    try:
        bot.unload_extension("cogs."+extension)
        print("Unloaded {}".format(extension))
        await ctx.send("Your prayers have been answered.")
    except Exception as error:
        print("{} cannot be unloaded. [{}]".format(extension,error))
        await ctx.send("Who do you think I am to command me as such!")

# Run bot
with open('token.txt','r') as f:
    lines = f.readlines()
    token = lines[0]

print("Running Bot")
print(token)
bot.run(token)
