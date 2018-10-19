#!/usr/bin/python3
import pygsheets

gc = pygsheets.authorize(service_file='./German words-0c5e5ad725e4.json')
sh = gc.open_by_key('10D-NsnwxiJUuELnpKxGdsjrwiiBKmrWtT5UlPFaGRTE')

def getWordsheet():
    TITLE = 'Words'
    return sh.worksheet('title', TITLE)

def initWordSheet():
    '''
    Creates a new worksheet for saving words
    if sheet does not exist
    '''
    try:
        wordsheet = getWordsheet()
    except pygsheets.WorksheetNotFound:
        wordsheet = sh.add_worksheet(TITLE)
    return wordsheet

def readWords():
    wordsheet = getWordsheet()
    return wordsheet.get_all_values()

def findWordsG2F(word, wordmatrix):
    '''

    Returns the sublist and the 0-indexed row number
    '''
    return (words for words in wordmatrix if words[0] == word),
        [words[0] for words in wordmatrix].index(word)
