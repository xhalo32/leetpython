#!/usr/bin/python3
import csv, re

def readFile(name):
    '''
    Takes in the file's name.
    Reads the file delimited with tabs and newlines.
    The file supports comments with //
    Returns a two-dimensional list of cells read from the given file.
    '''
    commentRe = re.compile('^//.*$')
    with open(name) as csvfile:
        return(list(filter(
            lambda row: len(row) is not 0 and commentRe.match(row[0]) is None,
            csv.reader(csvfile, delimiter='\t'))))

def convertSimpleDict(wordList):
    '''
    Takes in a list of sublists.
    Unpacks the 1st and the 2nd element in each sublist
    and returns a dictionary with all the first elements
    as the keys and second elements as the values.

    NOTE: Does not care about the rest of the elements
    that come after the second element in each sublist.
    '''
    return { german: finnish for (german, finnish, *rest) in wordList }

def invertDict(wordDict):
    return { v: k for (k, v) in wordDict.items() }
