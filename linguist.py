import json
from pathlib import Path
import random

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

def fopen(name):
    with open(name, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

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
    
def randomkey(words):
    if not words:
        print("No words in file")
        return None
    key = list(words.keys())
    random_key = random.choice(key)
    return random_key

filelist()

words = fopen(input("Enter a file name: ") + ".json")
first_key = next(iter(words))
print(first_key)
print(words[first_key]["translation"])
language = input("Podaj język: ")

if language == first_key:
    if first_key in words:
        del words[first_key]

    while True:
        randomword = randomkey(words)

        if words[randomword]["counter"] > 0:
            print(randomword + " = ", end="")
            guess = input("")
            if guess == words[randomword]["translation"]:
                print("Nice one")
                words[randomword]["counter"] -= 1
                if words[randomword]["counter"] <= 0:
                    del words[randomword]
            else:
                print("Wrong answer")
                print(f"Right answer: {words[randomword]["translation"]}")
                words[randomword]["counter"] += 1
        else:
            del words[randomword]


        if not words:
            break

elif language == words[first_key]["translation"]:
    if first_key in words:
        del words[first_key]

    while True:
        randomword = randomkey(words)

        if words[randomword]["counter"] > 0:
            print(words[randomword]["translation"] + " = ", end="")
            guess = input("")
            if guess == randomword:
                print("Nice one")
                words[randomword]["counter"] -= 1
            else:
                print("Wrong answer")
                print(f"Right answer: {randomword}")
                words[randomword]["counter"] += 1
        else:
            del words[randomword]
        if not words:
            break

