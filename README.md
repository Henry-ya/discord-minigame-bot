# Discord Mini Game Bot

This is a Discord bot that allows users to play games like Wordle and Blackjack directly within their Discord server 
## Features

- **Wordle**: A word guessing game where you have six attempts to guess a 5-letter word.
- **Blackjack**: A classic card game where the goal is to beat the dealer by getting a hand value as close to 21 as possible without exceeding it.

    *(Note) More games will be added in the future*

## Installation

### Prerequisites

- Python 3.7+
- `discord.py` library
- `discord-ui` library

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/discord-game-bot.git
   cd discord-game-bot
   ```

2. Install the required packages:

   ```bash
   pip install discord.py discord-ui
   ```

3. (Optional) Create a file named `.env` in the root directory of the project and add your Discord bot token:

   ```env
   DISCORD_BOT_TOKEN = your_discord_bot_token
   ```
     Or directly add the token into the         main file
   
   ```env
   bot.run('DISCORD_BOT_TOKEN')
   ```

4. Run the bot:

   ```bash
   python main.py
   ```

## Usage

### Starting the Bot

After running the bot script, the bot should be online in your Discord server.

*(Note) bot will go offline when script is stopped*

### Commands

#### General Commands

- `/start_game`: Starts a new game session. You will be prompted to choose between Wordle and Blackjack using buttons.

#### Wordle Commands

- `/guess_wordle <guess>`: Make a guess in the Wordle game.
- `/status_wordle`: Check the status of the current Wordle game.

#### Blackjack Commands

- `/hit`: Draw an additional card in Blackjack.
- `/stand`: Stand in Blackjack.
- `/double_down`: Double down in Blackjack.
- `/split`: Split cards in Blackjack.
- `/status_blackjack`: Check the status of the current Blackjack game.
