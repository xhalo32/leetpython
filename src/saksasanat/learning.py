#!/usr/bin/python

import pickle, time
pklfile = 'words.pickle'

def save(data):
    with open(pklfile, 'wb') as f:
        pickle.dump(data,f,pickle.HIGHEST_PROTOCOL)
    return data

def load():
    with open(pklfile, 'rb') as f:
        data = pickle.load(f)
    return data

def saveword(word, correct):
    data = load()
    data[word] = 
