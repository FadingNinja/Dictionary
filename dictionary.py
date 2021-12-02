import json
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def translate(w) :
    w = w.lower()

    if w in data :
        return data[w]

    elif len(get_close_matches(w, data.keys())[0]) :
        closestMatch = get_close_matches(w, data.keys())[0]
        yn = input(f"Did you mean {closestMatch} instead? Enter Y if yes, or N if no : ")
        yn = yn.lower()

        if yn == 'y' :
            return data[closestMatch]
        elif yn == 'n' :
            return "The word doesn't exist, please double check it."
        else :
            return "We didn't understand your entre."
    else :
        return "The word doesn't exist, please double check it."

word = input("Enter a word : ")
output = translate(word)

print(output)

input("Press ENTER to exit")