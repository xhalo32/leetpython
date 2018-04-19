#!/usr/bin/python

import pickle
pklfile = 'data.pickle'

data = {
	"Grönlanti" : { "country" : 1.0, "capital" : 1.0 }
}

def save(data):
	with open(pklfile, 'wb') as f:
		pickle.dump(data,f,pickle.HIGHEST_PROTOCOL)
	return data

def load():
	with open(pklfile, 'rb') as f:
		data = pickle.load(f)
	return data
