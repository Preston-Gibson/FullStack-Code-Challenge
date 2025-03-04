# FullStack-Code-Challenge
Code Challenge: Multi-Player Word Guessing Game with Dynamic Word Generation and
Web Interface
Objective:
We understand this is a challenging task, and we want to emphasize that the goal here is to give
you the opportunity to showcase your skills, learn new things, and demonstrate your problem-
solving abilities. We don’t expect everything to be perfect—don’t worry if you can’t complete
every part of the challenge. What matters most is your approach, how you tackle the different
aspects of the game, and how you solve problems along the way.
If you find that you can’t complete the entire challenge, feel free to submit what you have. This
gives us insight into your current level and potential, and we’re always interested in seeing how
you think and what you’ve learned. Remember, the challenge is meant to push your skills and
help you grow, not to discourage you. Good luck, and we look forward to seeing what you build!
Requirements:
Core Gameplay:
1. Welcome Screen:
o Display a welcome message with an option to either create a new game or join an
existing game.
2. Dynamic Word Generation:
o The game will fetch words dynamically from a public API (e.g., Wordnik API,
Datamuse API, or Dictionary API).
o Fetch a new word each time a new game starts. Ensure the word is filtered by length to
match the difficulty level.
3. Multi-Player Game Logic:
o Support two players competing in a word guessing game.
o Each player takes turns guessing a letter. The program should display the current word
status (with guessed letters revealed) after each guess.
o Players are given a limited number of incorrect guesses (e.g., 7 incorrect guesses).
o The first player to guess all the letters in the word wins. If both players run out of
guesses, the game ends in a draw.
4. User Interaction & Input Validation:
o Validate that the input is a single alphabetical character and ensure players are not
guessing the same letter repeatedly.
Additional Features:
1. Game History & High Scores:
o Once a game ends, store the game results in a simple database (e.g., SQLite or local
storage) to track high scores based on the fewest incorrect guesses.
o Track and display a leaderboard showing the top players based on the fewest incorrect
guesses.
2. Game Replay & Persistence:
o After a game ends, offer the option to start a new game or view Top Scores.
Technologies & Skills Involved:
1. Backend Development:
o Use a backend framework like Flask (Python) or Express (Node.js) to create an API and
serve the game logic.
o Use a database (SQLite or local storage) for storing game results and high scores.
2. Frontend Development:
o Build a web interface using HTML, CSS, and JavaScript (or a simple framework like
React.js) to create an interactive experience.
o The interface should update dynamically to reflect the game state (e.g., display the
word status, guesses, and remaining attempts).
3. API Integration:
o Integrate with a dictionary API to pull random words of varying lengths.
4. Optional Testing:
o If you have time and feel comfortable, you can write unit tests for the game logic,
including:
• Word validation (correct handling of guessed letters).
• Correct functionality of the game state (turn-taking, win condition, guess
tracking).
Extra Credit / Extensions:
1. AI Player (Optional):
o Allow a user to play against an AI. The AI can be implemented with a basic strategy,
such as guessing frequently used letters or trying random guesses when in doubt.
2. Multiple Difficulty Levels (Optional):
o Add the option to choose between easy, medium, and hard difficulty, which could affect
the word length and/or the complexity of the word (e.g., longer or more obscure words
for harder difficulty).
3. Mobile Responsiveness (Optional):
o Ensure that the game is mobile-responsive, so users can play it on their phones.
4. Word Hint System (Optional):
o Implement a hint system where a player can use one hint during a game (e.g., show one
correctly guessed letter or give a definition of the word).
Why This Challenge Is Relevant:
• Real-World Application:
o This challenge simulates a simple, interactive web application with real-world
applications like word fetching from an API and saving game data.
o You’ll get hands-on experience with key skills such as web frameworks, APIs, and
working with databases.
• Simple Yet Scalable:
o While simple, the game design offers room for you to extend your work, adding more
features and polishing your project as you go.
• Focus on Modern Development Skills:
o This challenge will test your ability to implement basic gameplay logic, connect to an
external API, and develop a basic web interface—skills that are essential for all
developers.
Example of Game Flow:
1. Start:
o Player 1 and Player 2 join the game.
o The game fetches a random word from the dictionary API (e.g., "astronaut").
2. Gameplay:
o Both players take turns guessing a letter. If Player 1 guesses "a", the display updates to
show: a _ _ _ _ _.
o If Player 2 guesses "z", it’s added to the list of incorrect guesses.
o The game continues until one player guesses the word correctly or both players run out
of attempts.
3. End:
o A winner is declared or the game is a draw.
o The game prompts the players to play again or view Top Scores.
