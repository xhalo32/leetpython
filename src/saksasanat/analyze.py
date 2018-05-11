#!/usr/bin/python

import learning, pprint

data = learning.load()

# pprint.pprint(data)
def safediv(a,b):
    if b: return a/b
    return 0

def getcorrect(word, data):
    l = [int(v["correct"]) for v in data[word]]
    return l

def get_per(word,data):
    l = getcorrect(word,data)
    return safediv(sum(l),len(l))

def sortmethod(item):
    # sort primarily on length of answers
    # then alphabetically
    return f"{chr(len(getcorrect(item,data)))}{item}"

sortedlist = sorted(data.keys(), key=sortmethod)

for item in sortedlist:
    print(f"{item}\n    {getcorrect(item,data)} {get_per(item,data)}")
