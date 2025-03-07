# WordGuessingGame serves to store game information and player guesses.
class WordGuessingGame:
    def __init__(self, word):
        self.word = word.lower()
        self.players = {
            1: {"guessed_letters": set(), "incorrect_guesses": set()},
            2: {"guessed_letters": set(), "incorrect_guesses": set()}
        }
        self.max_attempts = 7

    # Handles the logic for player guessing and criteria for finishing the game.
    # KNOWN ISSUES: Doesn't automaticaly take turns, doesn't change the blank spaces for the other player on change of player number,
    #               Game says "Game Over" whether you won or lost. Let's you try and guess before you've started the game.
    def guess(self, player, letter):
        letter = letter.lower()
        if player not in self.players:
            return {"error": "Invalid player number"}

        if letter in self.players[player]["guessed_letters"] or letter in self.players[player]["incorrect_guesses"]:
            return {"error": "Letter already guessed"}

        if letter in self.word:
            self.players[player]["guessed_letters"].add(letter)
        else:
            self.players[player]["incorrect_guesses"].add(letter)

        return {
            "word_status": self.get_word_display(player),
            "incorrect_guesses": list(self.players[player]["incorrect_guesses"]),
            "game_over": self.is_game_over(player)
        }

    # Contains the logic for displaying a word with "_" for unguessed letters remaining.
    def get_word_display(self, player):
        return ''.join([char if char in self.players[player]["guessed_letters"] else '_' for char in self.word])

    # Returns the number of incorrect guesses for a player.
    def get_incorrect_guess_count(self, player):
        return len(self.players[player]["incorrect_guesses"])

    # Handles the logic for ending the game if allowable guesses are exceeded or the player guesses the word.
    def is_game_over(self, player):
        """Checks if the game is over for a player (win or lose)"""
        return set(self.word) == self.players[player]["guessed_letters"] or self.get_incorrect_guess_count(player) >= self.max_attempts
