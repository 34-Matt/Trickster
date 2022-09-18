import os
import pickle
from discord import Embed, File
from chessdotcom import get_player_profile, get_player_stats, Client

import pprint
printer = pprint.PrettyPrinter()

Client.config["headers"]["User-Agent"] = (
    "Trickster Discord Bot. "
    "Bot information can be found at https://github.com/34-Matt/Trickster."
)

# Handles Databases
CHESSDATABASENAME = os.path.join('databases', 'chess.pickle')
if os.path.exists(CHESSDATABASENAME):
    CHESSDATABASE = pickle.load(open(CHESSDATABASENAME, "rb"))
else:
    CHESSDATABASE = {}

def updateChessDatabase(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        pickle.dump(CHESSDATABASE, open(CHESSDATABASENAME, "wb"))
    return wrapper


# Player Extraction
def discord2chess(user):
    if user in CHESSDATABASE.keys():
        return CHESSDATABASE[user]
    else:
        return user

def getPlayerRating(stats, gameMode):
    '''Extracts the game rating for a game mode from loaded stats
    '''
    if gameMode == 'puzzle_rush':
        return stats[gameMode]['best']['score']
    elif gameMode == 'tactics':
        return stats[gameMode]['highest']['rating']
    else:
        return stats[gameMode]['last']['rating']


# Elo Calculations
# All functions begin with the player's and opponent's ratings
def performance(player, opponent, wins=1, losses=0, ties=0):
    '''Calculates the performance rating for a series of games between an opponent.
    wins := The number of games won against the opponent
    losses := The number of games lost against the opponent
    ties := The number of games tied against the opponent
    '''
    games = wins + losses + ties
    return (opponent + 400 * (wins - losses)) / games

def expectation(player, opponent):
    '''Calculates the expectation score of the player winning
    '''
    return 1 / (1 + 10 ** ((opponent - player) /400))

def expectedMultiplier(player, opponent):
    '''Calculates the how many times greater the players expected score is from the opponent
    '''
    return 10 ** ((player - opponent) / 400)

def tournamentAdjust(expected, actual, kFactor=32):
    '''Calcuates the adjustment to the player's after a tournament
    expected := the expect score of the tournament [sum(expectations)]
    actual := the score after the tournament [sum(win=1, tie=0.5, loss=0)]
    kFactor := the adjustment score, or score ante [32 for beginners (default), 16 for masters]
    '''
    return kFactor * (actual - expected)


# Embedding Functions
def displayPlayer(playerID, debug=False):

    profile = get_player_profile(playerID).json['player']
    stats = get_player_stats(playerID).json['stats']

    if debug:
        for k, v in profile.items():
            print(k, ': ', v)
        print()
        for k, v in stats.items():
            print(k, ': ', v)
    
    embed = Embed(title=profile['username'],
        description="Here is the stat information for [{}]({})".format(profile['username'], profile['url']))
    if 'avatar' in profile['keys']:
        embed.set_thumbnail(url=profile['avatar'])
    
    atleastOne = False
    if 'chess_daily' in stats.keys():
        embed.add_field(name="Daily", value = stats['chess_daily']['last']['rating'], inline=False)
        atleastOne = True
    if 'chess_rapid' in stats.keys():
        embed.add_field(name="Rapid", value = stats['chess_rapid']['last']['rating'], inline=False)
        atleastOne = True
    if 'chess_bullet' in stats.keys():
        embed.add_field(name="Bullet", value = stats['chess_bullet']['last']['rating'], inline=False)
        atleastOne = True
    if 'chess_blitz' in stats.keys():
        embed.add_field(name="Blitz", value = stats['chess_blitz']['last']['rating'], inline=False)
        atleastOne = True
    if not atleastOne:
        embed.add_field(name="Game Status", value = 'This player does not have a score on chess.com', inline=False)
    embed.add_field(name="Best Tactics", value = stats['tactics']['highest']['rating'], inline=False)

    return embed

def comparePlayers(playerName, opponentName):
    '''Compares the performance of a player against their opponent
    '''
    playerStats = get_player_stats(playerName).json['stats']
    opponentStats = get_player_stats(opponentName).json['stats']

    embed = Embed(title=f'{playerName} vs {opponentName}',
        description=f'Expected outcome between these two players')
    file = File(os.path.join('Images', 'queen.png'), "queen.png")
    embed.set_thumbnail(url='attachment://queen.png')

    for match in ['chess_blitz', 'chess_rapid', 'chess_bullet', 'chess_daily']:
        playerRating = getPlayerRating(playerStats, match)
        opponentRating = getPlayerRating(opponentStats, match)
        embed.add_field(name=match, value=f"Expected {playerName} to win {100*expectation(playerRating, opponentRating)}% of games")

    return file, embed

if __name__ == '__main__':
    player = 2000
    oppon = 1800
    print(expectation(player, oppon))
    print(expectedMultiplier(player, oppon))
