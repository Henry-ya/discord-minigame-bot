import discord
from discord.ext import commands
from discord import Button, ButtonStyle
from games.wordle import WordleGame, start_game_command as start_wordle_game, guess_command as guess_wordle, status_command as status_wordle
from games.blackjack import BlackjackGame, start_game_command as start_blackjack_game, hit_command, stand_command, double_down_command, split_command, status_command as status_blackjack

# Set up the bot with the required intents
intents = discord.Intents.default()
intents.message_content = True

# create / cm
bot = commands.Bot(command_prefix='/', intents=intents)

# to keep track of game states per channel
games = {}

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

class GameSelectView(discord.ui.View):
    def __init__(self, games, channel_id):
        super().__init__()
        self.games = games
        self.channel_id = channel_id

    @discord.ui.button(label="Wordle", style=ButtonStyle.primary)
    async def wordle_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.channel_id in self.games:
            await interaction.response.send_message("A game is already in progress in this channel.", ephemeral=True)
        else:
            self.games[self.channel_id] = WordleGame()
            await interaction.response.send_message("Wordle game started! You have 6 attempts to guess the 5-letter word.")
            await interaction.message.delete()

    @discord.ui.button(label="Blackjack", style=ButtonStyle.success)
    async def blackjack_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.channel_id in self.games:
            await interaction.response.send_message("A game is already in progress in this channel.", ephemeral=True)
        else:
            self.games[self.channel_id] = BlackjackGame()
            await interaction.response.send_message("Blackjack game started! Use commands to play.")
            await interaction.message.delete()

@bot.command(name='start_game', description='Start a new game')
async def start_game_command(ctx):
    view = GameSelectView(games, ctx.channel.id)
    await ctx.send("Please select a game to start:", view=view)

# Register commands for Wordle and Blackjack games (buttons enable these commands after game start)
@bot.command(name='guess_wordle', description='Make a guess in the Wordle game')
async def guess_wordle_command(ctx, guess: str):
    await guess_wordle(ctx, guess, games)

@bot.command(name='status_wordle', description='Check the status of the current Wordle game')
async def status_wordle_command(ctx):
    await status_wordle(ctx, games)

@bot.command(name='hit', description='Draw an additional card in Blackjack')
async def hit_command(ctx):
    await hit_command(ctx, games)

@bot.command(name='stand', description='Stand in Blackjack')
async def stand_command(ctx):
    await stand_command(ctx, games)

@bot.command(name='double_down', description='Double down in Blackjack')
async def double_down_command(ctx):
    await double_down_command(ctx, games)

@bot.command(name='split', description='Split cards in Blackjack')
async def split_command(ctx):
    await split_command(ctx, games)

@bot.command(name='status_blackjack', description='Check the status of the current Blackjack game')
async def status_blackjack_command(ctx):
    await status_blackjack(ctx, games)

bot.run('token here') #enter your own token here
