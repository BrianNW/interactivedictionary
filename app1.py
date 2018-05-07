import json

data = json.load(open("data.json"))

def translate(word):
    # counting for nonexistent words
    if w in data:
        return data[word]
    else:
        return "Word doesn't exist.  Please double check it."

word = input("Enter word: ")

print(translate(word))
