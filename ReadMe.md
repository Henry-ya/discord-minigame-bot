# Discord Games Bot

This is a Discord bot that allows users to play games like Wordle and Blackjack within their Discord server. The bot uses slash commands for interaction and provides an engaging way to play these games with friends.

## Features

- **Wordle**: A word guessing game where players have six attempts to guess a five-letter word.
- **Blackjack**: A classic card game where players try to reach 21 points without going over, using emoji poker cards.

  **More mini games coming soon**
## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/discord-games-bot.git
    cd discord-games-bot
    ```

2. **Install Dependencies**

    Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Your Discord Bot**

    - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
    - Create a new application and add a bot to it.
    - Copy the bot token and replace `'YOUR_DISCORD_BOT_TOKEN'` in `bot.py` with your actual bot token.

5. **Run the Bot**

    ```bash
    python main.py
    ```

## Usage

1. **Invite the Bot to Your Server**

    - Use the OAuth2 URL Generator in the Discord Developer Portal to generate an invite link for your bot.
    - Make sure to select the required permissions for the bot.

2. **Wordle Commands**

    - `/start_wordle`: Start a new Wordle game.
    - `/guess_wordle <word>`: Make a guess in the Wordle game.
    - `/status_wordle`: Check the status of the current Wordle game.

3. **Blackjack Commands**

    - `/start_blackjack`: Start a new Blackjack game.
    - `/hit`: Draw an additional card in Blackjack.
    - `/stand`: Stand in Blackjack.
    - `/double_down`: Double down in Blackjack.
    - `/split`: Split cards in Blackjack (if applicable).
    - `/status_blackjack`: Check the status of the current Blackjack game.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or new features to add.

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- credits to [DenverCoder1](https://github.com/DenverCoder1) for his inspiration and word list 
- Thanks to the [Discord.py](https://github.com/Rapptz/discord.py) library for providing the foundation for building Discord bots.
