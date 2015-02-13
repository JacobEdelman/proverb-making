import json
from random import choice
import sys
f = open("proverbs-app.antjan.us.json")
proverb_text = json.load(f)
tokens = sum([i.split(" ") for i in proverb_text], [])
while True:
    raw_input("")
    proverb = choice(proverb_text).split(" ")[0]
    while proverb[-1]!=  '.':
        proverb += " " + tokens[choice([i[0] for i in enumerate(tokens) if i[1] == proverb.split(" ")[-1]])+1]
    print proverb.encode('ascii','ignore')
    sys.stdout.flush()
