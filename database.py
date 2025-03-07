import sqlite3

DB_FILE = "game_history.db"

# Initializes the database table if it doesn't exist already.
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT,
            incorrect_guesses INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Saves the game's results.
# Known issue: It doesn't record the second players number of guesses. Doesn't display player name or number.
def save_game_result(game_id, word, incorrect_guesses):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO leaderboard (word, incorrect_guesses) VALUES (?, ?)", (word, incorrect_guesses))
    conn.commit()
    conn.close()

# Retrieves the leaderboard as the name implies.
# Known issue: It doesn't display the second player's number of guesses. Doesn't display player name or number.
def get_leaderboard():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT word, incorrect_guesses FROM leaderboard ORDER BY incorrect_guesses ASC LIMIT 5")
    scores = cursor.fetchall()
    conn.close()
    return [{"word": row[0], "incorrect_guesses": row[1]} for row in scores]

# Initialize the database when the app starts
init_db()
