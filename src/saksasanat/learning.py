#!/usr/bin/python

import pickle, time, random
from numpy import log
pklfile = 'words.pickle'

def save(data):
    with open(pklfile, 'wb') as f:
        pickle.dump(data,f,pickle.HIGHEST_PROTOCOL)
    return data

def load():
    try:
        with open(pklfile, 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError:
        return dict()
    return data

def saveword(word, correct, language):
    data = load()
    dat = { "timestamp" : time.time(),
            "correct" : correct,
            "answer_language" : language}
    # if not word in data.keys(): data[word] = []
    assert word in data.keys()
    data[word].append(dat)`
    save(data)

def fillempty(words):
    data = load()
    for k,v in words:
        if not k in data.keys():
            data[k] = []
    save(data)

def get_per(word):
    if len(word[1]) == 0: return 0.0
    sum([int(d['correct']) for d in word[1]]) / len(word[1])

def order(words, data):
    sortdatalist = sorted(random.shuffle(data.items()), key=get_per)
    newl = []
    # fill with new words
    for k,v in words.items():
        if not k in data.keys():
            newl.append((k,v))
    # add sorted words
    for w,dat in sortdatalist:
        if w in words.keys():
            newl.append((w,words[w]))
    return newl

def get_random_word(wl, median):
    weight = random.random()**(log(0.5)/log(1.-0.5*median-0.01))
    return wl[weight*len(wl)]

def shuff(words, number, repeats):
    data = load()
    l = []
    wl = order(words,data)
    median_per = get_per(wl[len(wl)//2])

    while 1:
        if len(l) == number:
            return l
        k,v = get_random_word(wl, median_per)
        if len(data[k]):
            if not data[k][-1]['correct']:
                l.append()
        else:
            l.append(()
        if random.random() > get_per(w):
