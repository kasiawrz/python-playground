import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    dict_keys = data.keys()

    if word in data:
        return data[word]

    suggestion = get_close_matches(word, dict_keys, 1, cutoff=0.8)
    if suggestion:
        return "Please double check your input. Did you mean: %s?" % suggestion[0]
    else:
        return "The word doesn't exist"


word = input("Enter word: ")

print(translate(word))
