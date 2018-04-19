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
	'völlig' : 'täysin',
	'erschöpft' : 'uupunut',
	'hin/fallen' : 'kaatua',
	'eher' : 'pikemminkin',
	'trotzdem' : 'siitä huolimatta',
	'etwas Warmes' : 'jotain lämmintä',
	'die Toilette' : 'vessa',
	'der Skilift' : 'hiihtohissi',
	'heiße Schokolade' : 'kuuma kaakao',
	'das Stück' : 'pala',
	'der Karottenkuchen' : 'porkkanakakku',
	'auf dem Tisch' : 'pöydällä',
	'liegen' : 'maata, sijaita',
	'der Prospekt' : 'esite',
	'das Skigebiet' : 'hiihtokeskus',
	'vor/stellen' : 'esitellä',
	'berühmt' : 'kuuluisa',
	'vorher' : 'aikaisemmin',
	'unten' : 'alhaalla',
	'der See' : 'järvi',
	'der Sauerstoff' : 'happi',
	'kriegen' : 'saada',
	'harmlos' : 'harmiton',
	'esrt mal' : 'ensin',
	'die blauen Flecken' : 'mustelmat',
	'zählen' : 'laskea',
	'soll das heißen' : 'tarkoittaako se',
	'steil' : 'jyrkkä',
	'im Gegenteil' : 'päinvastoin',
	'weh' : 'kipeä',
	'weh/tun' : 'sattua',
	'der Hintern' : 'takamus',
	'auf jeden Fall' : 'joka tapauksessa',
	'sich interessieren' : 'olla kiinnostunut',
}

# flip keys/values
sanat = dict((v,k) for k,v in sanat.items())
