from flask import Flask, render_template, request, jsonify
from wordApi import get_random_word
from gameLogic import WordGuessingGame
from database import save_game_result, get_leaderboard

app = Flask(__name__)

# Store active games
games = {}

# Defines the home screen
@app.route('/')
def home():
    return render_template('index.html')

# Starts the process for a new game allowing guesses to be made and generates a new word.
@app.route('/new_game', methods=['POST'])
def new_game():
    """Starts a new game with a random word"""
    word = get_random_word()
    game_id = len(games) + 1
    games[game_id] = WordGuessingGame(word)

    return jsonify({'game_id': game_id, 'word_length': len(word)})

# Handles the logic for player guessing and criteria for finishing the game.
# KNOWN ISSUES: Doesn't automaticaly take turns, doesn't change the blank spaces for the other player on change of player number,
#               Game says "Game Over" whether you won or lost. Let's you try and guess before you've started the game.
@app.route('/guess', methods=['POST'])
def guess_letter():
    """Handles a player's letter guess"""
    data = request.json
    game_id = data.get('game_id')
    player = data.get('player')  # Player 1 or Player 2
    letter = data.get('letter')

    if game_id not in games:
        return jsonify({"error": "Invalid game ID"}), 400

    game = games[game_id]
    result = game.guess(player, letter)

    if result["game_over"]:
        save_game_result(game_id, game.word, game.get_incorrect_guess_count(player))
        del games[game_id]  # Remove finished game from active games

    return jsonify(result)

# Retrieves leaderboard information from the database using the imported get_leaderboard function.
@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    scores = get_leaderboard()
    return jsonify(scores)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
