#!/usr/bin/python

def shuff(d):
	from random import random
	l=[]
	# make flat list
	dl=[b for a in [list(d[i].items()) for i in d.keys()] for b in a]
	lf=[]
	for a,b in dl:
	while 1:
		i=int(len(lf)*random())%len(lf)
		if len(l)==len(lf): break
		if lf[i] in l: continue
		l.append(lf[i])
	return l

prepositiot = {
	'läpi, kautta' : 'durch',
	'varten, hintaan, -lle' : 'für',
	'vastaan, päin' : 'gegen',
	'ilman' : 'ohne',
	'ympäri' : 'um (herum',

	'läpi, kautta' : 'durch',
	'läpi, kautta' : 'durch',
	'läpi, kautta' : 'durch',
	'läpi, kautta' : 'durch',
	'läpi, kautta' : 'durch',
	'läpi, kautta' : 'durch',
	'läpi, kautta' : 'durch',
}
