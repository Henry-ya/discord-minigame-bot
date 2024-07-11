import random
import discord
import os


class WordleGame:
    def __init__(self):
        self.word = random.choice(self.load_words)
        self.attempts = 6
        self.history = []
        self.incorrect_letters = set()
    
    def load_words(self):
        words_file = os.path.join(os.path.dirname(__file__), 'wordlist.txt')
        with open(words_file, 'r') as file:
            words = [line.strip() for line in file.readlines()]
        return words

    def guess(self, guess_word):
        if len(guess_word) != 5:
            return "Guess must be a 5-letter word."
        if not guess_word.isalpha():
            return "Guess must only contain letters."
        
        self.attempts -= 1
        result, feedback = self.check_guess(guess_word)
        self.history.append((guess_word, feedback))
        
        if guess_word == self.word:
            return f"🎉 Congratulations! You guessed the word: **{self.word}**"
        elif self.attempts == 0:
            return f"💀 Game over! The word was: **{self.word}**"
        else:
            return result

    def check_guess(self, guess_word):
        result = []
        feedback = []
        word_letters = list(self.word)
        for i in range(len(guess_word)):
            if guess_word[i] == self.word[i]:
                result.append("🟩")
                feedback.append(f"{guess_word[i]} (correct)")
                word_letters[i] = None
            elif guess_word[i] in word_letters:
                result.append("🟨")
                feedback.append(f"{guess_word[i]} (wrong position)")
                word_letters[word_letters.index(guess_word[i])] = None
            else:
                result.append("🟥")
                feedback.append(f"{guess_word[i]} (incorrect)")
                self.incorrect_letters.add(guess_word[i])
        return ' '.join(result), ' '.join(feedback)


async def start_game_command(interaction: discord.Interaction, games):
    channel = interaction.channel
    if channel.id in games:
        await interaction.response.send_message("A game is already in progress in this channel.")
    else:
        games[channel.id] = WordleGame()
        await interaction.response.send_message("Wordle game started! You have 6 attempts to guess the 5-letter word. Use `/guess <word>` to make a guess.")

async def guess_command(interaction: discord.Interaction, guess: str, games):
    channel = interaction.channel
    if channel.id not in games:
        await interaction.response.send_message("No game is currently in progress. Use `/start` to start a new game.")
    else:
        game = games[channel.id]
        result = game.guess(guess.lower())
        if "Congratulations" in result or "Game over" in result:
            await interaction.response.send_message(result)
            del games[channel.id]
        else:
            await interaction.response.send_message(result)
            await interaction.followup.send(f"Attempts remaining: {game.attempts}\nIncorrect letters: {' '.join(game.incorrect_letters)}")

async def status_command(interaction: discord.Interaction, games):
    channel = interaction.channel
    if channel.id not in games:
        await interaction.response.send_message("No game is currently in progress. Use `/start` to start a new game.")
    else:
        game = games[channel.id]
        history = '\n'.join([f"{attempt}: {result}" for attempt, result in game.history])
        await interaction.response.send_message(f"Game status:\n{history}\nAttempts remaining: {game.attempts}\nIncorrect letters: {' '.join(game.incorrect_letters)}")
