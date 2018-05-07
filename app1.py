import json

# Makes the program suggest similar words
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    w = w.lower()
    # counting for nonexistent words
    if w in data:
        return data[w]
    # initializes suggestion
    elif get_close_matches(w, data.keys())
    else:
        return "Word doesn't exist.  Please double check it."

word = input("Enter word: ")

print(translate(word))
