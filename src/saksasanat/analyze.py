#!/usr/bin/python

import learning, pprint

data = learning.load()

# pprint.pprint(data)

for word,values in data.items():
    l = [int(v["correct"]) for v in values]
    a = sum(l)
    b = len(values)
    print(f"{word}\n    {l} {a/b}")
