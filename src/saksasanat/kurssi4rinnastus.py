#!/usr/bin/python

def shuff(d):
	from random import random
	l=[]
	lf=list(d.items())
	for a in d:
		while 1:
			i=int(len(lf)*random())%len(lf)
			if len(l)==len(lf): break
			if lf[i] in l: continue
			l.append(lf[i])
	return l

sanat = {
	'mutta': 'aber',
	'sillä': 'denn',
	'tai': 'oder',
	'vaan': 'sondern',
	'joko - tai': 'entweder - oder',
	'ei ainoastaan - vaan myös': 'nicht nur - sondern auch',
        'sekä - että': 'sowohl - als auch',
        'osaksi - osaksi': 'teils - teils',
	'ei - eikä': 'weder - noch',
}
