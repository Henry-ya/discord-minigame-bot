import random
import discord

# define card values/type to emojies
CARD_SUITS = {
    'hearts': '♥️',
    'diamonds': '♦️',
    'clubs': '♣️',
    'spades': '♠️'
}

CARD_VALUES = {
    2: '2️⃣', 3: '3️⃣', 4: '4️⃣', 5: '5️⃣', 6: '6️⃣',
    7: '7️⃣', 8: '8️⃣', 9: '9️⃣', 10: '🔟',
    11: '🅰️', 12: '2️⃣', 13: '3️⃣', 14: '4️⃣'
}

class BlackjackGame:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.player_turn = True
        self.game_over = False
        self.result = ""

    def create_deck(self):
        deck = []
        for suit, emoji in CARD_SUITS.items():
            for value, emoji_value in CARD_VALUES.items():
                deck.append((suit, value, emoji, emoji_value))
        random.shuffle(deck)
        return deck

    def deal_cards(self):
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop(), self.deck.pop()]

    def hit(self):
        if self.player_turn:
            self.player_hand.append(self.deck.pop())
            if self.calculate_hand_value(self.player_hand) > 21:
                self.result = "You bust! Dealer wins."
                self.game_over = True
                self.player_turn = False
        else:
            return "It's not your turn."

    def stand(self):
        if self.player_turn:
            self.player_turn = False
            self.dealer_play()
        else:
            return "It's not your turn."

    def double_down(self):
        if self.player_turn:
            self.player_hand.append(self.deck.pop())
            self.player_turn = False
            self.dealer_play()
        else:
            return "It's not your turn."

    def split(self):
        if self.player_turn and self.player_hand[0][1] == self.player_hand[1][1]:
            self.player_hand = [self.player_hand[0], self.deck.pop()]
            self.split_hand = [self.player_hand[1], self.deck.pop()]
            self.player_turn = True

    def dealer_play(self):
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.pop())
        self.calculate_result()

    def calculate_hand_value(self, hand):
        value = sum(card[1] for card in hand)
        num_aces = sum(1 for card in hand if card[1] == 11)
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value

    def calculate_result(self):
        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        if player_value > 21:
            self.result = "You bust! Dealer wins."
        elif dealer_value > 21:
            self.result = "Dealer busts! You win."
        elif player_value > dealer_value:
            self.result = "You win!"
        elif player_value < dealer_value:
            self.result = "Dealer wins."
        else:
            self.result = "It's a tie."

        self.game_over = True

    def format_hand(self, hand):
        return ' '.join(f"{card[2]} {CARD_VALUES[card[1]]}" for card in hand)

    def get_game_status(self):
        player_hand_str = self.format_hand(self.player_hand)
        dealer_hand_str = self.format_hand(self.dealer_hand)
        return f"Your hand: {player_hand_str}\nDealer's hand: {dealer_hand_str}\n\nResult: {self.result}"

async def start_game_command(interaction: discord.Interaction, games):
    channel = interaction.channel
    if channel.id in games:
        await interaction.response.send_message("A game is already in progress in this channel.")
    else:
        games[channel.id] = BlackjackGame()
        games[channel.id].deal_cards()
        await interaction.response.send_message("Blackjack game started! Use `/hit`, `/stand`, `/double_down`, and `/split` to play.")

async def hit_command(interaction: discord.Interaction, games):
    channel = interaction.channel
    if channel.id not in games:
        await interaction.response.send_message("No game is currently in progress. Use `/start_blackjack` to start a new game.")
    else:
        game = games[channel.id]
        game.hit()
        if game.game_over:
            await interaction.response.send_message(game.get_game_status())
            del games[channel.id]
        else:
            await interaction.response.send_message(game.get_game_status())

async def stand_command(interaction: discord.Interaction, games):
    channel = interaction.channel
    if channel.id not in games:
        await interaction.response.send_message("No game is currently in progress. Use `/start_blackjack` to start a new game.")
    else:
        game = games[channel.id]
        game.stand()
        if game.game_over:
            await interaction.response.send_message(game.get_game_status())
            del games[channel.id]
        else:
            await interaction.response.send_message(game.get_game_status())

async def double_down_command(interaction: discord.Interaction, games):
    channel = interaction.channel
    if channel.id not in games:
        await interaction.response.send_message("No game is currently in progress. Use `/start_blackjack` to start a new game.")
    else:
        game = games[channel.id]
        game.double_down()
        if game.game_over:
            await interaction.response.send_message(game.get_game_status())
            del games[channel.id]
        else:
            await interaction.response.send_message(game.get_game_status())

async def split_command(interaction: discord.Interaction, games):
    channel = interaction.channel
    if channel.id not in games:
        await interaction.response.send_message("No game is currently in progress. Use `/start_blackjack` to start a new game.")
    else:
        game = games[channel.id]
        game.split()
        if game.game_over:
            await interaction.response.send_message(game.get_game_status())
            del games[channel.id]
        else:
            await interaction.response.send_message(game.get_game_status())

async def status_command(interaction: discord.Interaction, games):
    channel = interaction.channel
    if channel.id not in games:
        await interaction.response.send_message("No game is currently in progress. Use `/start_blackjack` to start a new game.")
    else:
        game = games[channel.id]
        await interaction.response.send_message(game.get_game_status())
