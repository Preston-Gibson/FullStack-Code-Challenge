import requests
import random

# Retrieves a random word from the datamuse api. Nods to Lord of the Rings if it fails.
def get_random_word():
    """Fetch a truly random word from the Datamuse API"""
    try:
        response = requests.get("https://api.datamuse.com/words?max=50&ml=random")
        words = response.json()

        if words:
            # Pick a truly random word from the list
            return random.choice(words)["word"]
        else:
            return "shire"  # A fallback word in case of an empty response

    except Exception as e:
        print(f"Error fetching word: {e}")
        return "hobbit"  # Fallback word in case of API failure