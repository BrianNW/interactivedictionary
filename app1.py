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
    elif len(get_close_matches(w, data.keys())) > 0;
        yn input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        if yn == "N":
            return "The word doesn't exist.  Please double check it."
        else:
            return "Input unrecognized. Try again"
    else:
        return "Word doesn't exist.  Please double check it."

word = input("Enter word: ")

print(translate(word))
