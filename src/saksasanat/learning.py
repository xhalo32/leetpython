#!/usr/bin/python

import pickle, time, random
from numpy import log, e
pklfile = 'words.pickle'

def save(data):
    '''
    Saves a dictionary containing the data into a pickle file
    '''
    with open(pklfile, 'wb') as f:
        pickle.dump(data,f,pickle.HIGHEST_PROTOCOL)
    return data

def load():
    '''
    Returns the dictionary from the pickle file
        If the file doesn't exist returns an empty dictionary
    '''
    try:
        with open(pklfile, 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError:
        return dict()
    return data

def saveword(word, correct, language):
    '''
    Saves a new sample of {timestamp, correct, answer_language}
        to the pickle file
    Assumes that the word is already in the dictionary
    '''
    data = load()
    dat = { "timestamp" : time.time(),
            "correct" : correct,
            "answer_language" : language}
    # if not word in data.keys(): data[word] = []
    assert word in data.keys()
    data[word].append(dat)
    save(data)

def fillempty(words):
    '''
    Appends to the dictionary with valid empty words
    Should be used before saving data samples to the dictionary
    '''
    data = load()
    for k,v in words.items():
        if not k in data.keys():
            data[k] = []
    save(data)

def get_per(word):
    '''
    Takes in a key-value pair from the dictionary
    Returns the per cent of how many samples are correct
    '''
    return _get_per(word[1])

def _get_per(samplelist):
    '''
    Takes in a list of samples from a word of the dictionary
    Return the per cent of how many samples are correct (from the last 4 samples)
    '''
    samplelist = samplelist[-4:]
    if len(samplelist) == 0: return 0.0
    return sum([int(d['correct']) for d in samplelist]) / len(samplelist)

def get_median(wl):
    '''
    Takes in the word-pair list ordered according to their per cent correct
    Returns the left-alligned middle element of the list
    '''
    return wl[len(wl)//2]

def order(words, data):
    '''
    Takes in a word list
    Takes in the pickled data
    Returns the word list ordered according to the elements' per cent correct
    '''
    l = list(data.items())
    random.shuffle(l)
    sortdatalist = sorted(l, key=get_per)
    newl = []
    for w,dat in sortdatalist:
        if w in words.keys():
            newl.append((w,words[w]))
    return newl

def get_random_word(wl, median):
    '''
    Takes in the ordered word list and the median per cent
    Returns a random word from the word list
    '''
    r = random.random()
    weight = e**(-10*(1-median)*r)*(1-r)
    return wl[int(weight*len(wl))]

def shuff(words, number, repeats):
    '''
    Takes in a word list, a number, a boolean value representing if an element can be in the returned list more than once
    Returns a list of words with length 'number' with words returned from 'get_random_word' function
    '''
    data = load()
    wl = order(words,data)
    median_per = _get_per(data[get_median(wl)[0]])

    l = []
    while 1:
        if len(l) == number: return l
        wl = order(words,data)
        w = get_random_word(wl, median_per)
        if not repeats and w in l: continue
        l.append(w)

def stats(words):
    data = load()
    wl = order(words,data)
    median_per = _get_per(data[get_median(wl)[0]])
    return "median: {}".format(median_per)
