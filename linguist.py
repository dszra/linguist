import json
from pathlib import Path
import random

# future feature for adding dictionaries for learning
def fwrite(name):
    words = {
        "it": {"translation": "pl", "counter": 0, "block": 1},
        "ciao": {"translation": "cześć", "counter": 1, "block": 0},
        "nome": {"translation": "imię", "counter": 1, "block": 0},
        "mi chiamo": {"translation": "nazywam się", "counter": 1, "block": 0}
    }

    with open("lekcja1.json", "w", encoding="utf-8") as f:
        json.dump(words, f, indent=4, ensure_ascii=False)
fwrite("name")


# function to open a json file by name
def fopen(name):
    with open(name, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


# function for displaying json files (dictionaries) in the program folder
def filelist(fpath="."):
    dirfile = Path(fpath)

    if not dirfile.is_dir():
        print("Directory doesn't exist")
        return
    json_file = list(dirfile.glob("*.json"))

    if not json_file:
        print("No file in directory")
    else:
        print("Files list: \n")
        for n, jsonf in enumerate(json_file, start=1):
            print(f"{n}. {jsonf.name}")
    
        return json_file

# function for drawing a word from a dictionary
def randomkey(words):
    if not words:
        print("No words in file")
        return None
    key = list(words.keys())
    random_key = random.choice(key)
    return random_key


filelist()

words = fopen(input("Enter a file name: ") + ".json") # opening json file by name
first_key = next(iter(words)) # downloading a key that has the languages ​​to be learned saved in this file
# print languages from file
print(first_key)
print(words[first_key]["translation"])
language = input("Specify language: ") #select language

if language == first_key: # action according to key
    if first_key in words: #deleting language key
        del words[first_key]

    while True: # while for guessing word by key
        randomword = randomkey(words) # drawing word

        if words[randomword]["counter"] > 0: # words with counter=0 should be deleted, but if are not, here we skip them
            print(randomword + " = ", end="")
            guess = input("")
            if guess == words[randomword]["translation"]: # if right answer substract 1 from word counter
                print("Nice one")
                words[randomword]["counter"] -= 1
                if words[randomword]["counter"] <= 0:
                    del words[randomword]
            else: # if wrong answer add 1 to word counter
                print("Wrong answer")
                print(f"Right answer: {words[randomword]["translation"]}")
                words[randomword]["counter"] += 1
        else: # delete word with counter = 0
            del words[randomword]


        if not words: # end if there are not words in dictionary anymore
            break

elif language == words[first_key]["translation"]: # action according to value
    if first_key in words: # deleting language key
        del words[first_key]

    while True: # while for guesing word by value
        randomword = randomkey(words)

        if words[randomword]["counter"] > 0: # words with counter=0 should be deleted, but if are not, here we skip them
            print(words[randomword]["translation"] + " = ", end="")
            guess = input("")
            if guess == randomword: # if right answer substract 1 from word counter
                print("Nice one")
                words[randomword]["counter"] -= 1
            else: # if wrong answer add 1 to word counter
                print("Wrong answer")
                print(f"Right answer: {randomword}")
                words[randomword]["counter"] += 1
        else: # delete word with counter = 0
            del words[randomword]
        if not words: # end if there are not words in dictionary anymore
            break

