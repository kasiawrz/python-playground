import json

date = json.load(open('data.json')

def translate(word):
   return data[word]

word = input('Enter word: ')

print(translate(word))
