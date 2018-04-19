#!/usr/bin/python

def shuff(d):
	from random import random
	l=[]
	# make flat list
	dl=[b for a in [list(d[i].items()) for i in d.keys()] for b in a]
	lf=[]
	for a,b in dl:
		if isinstance(b,str): lf.append((a,b))
		else:
			for key,val in b.items():
				if isinstance(val,str): lf.append(('{} ({})'.format(a,key),val))
				else:
					for key2,val2 in val.items():
						lf.append(('{} ({} {})'.format(a,key,key2),val2))
	while 1:
		i=int(len(lf)*random())%len(lf)
		if len(l)==len(lf): break
		if lf[i] in l: continue
		l.append(lf[i])
	return l

pronominit = {
	'nominatiivi':{
		'minä':'ich',
		'sinä':'du',
		'hän':{
			'maskuliini':'er',
			'neutraali':'es',
			'feminiini':'sie',
		},
		'me':'wir',
		'te':'ihr',
		'he':'sie',
		'Te':'Sie',
	},
	'allatiivi':{
		'minulle':'mir',
		'sinulle':'dir',
		'hänelle':{
			'maskuliini':'ihm',
			'neutraali':'ihm',
			'feminiini':'ihr',
		},
		'meille':'uns',
		'teille':'euch',
		'heille':'ihnen',
		'Teille':'Ihnen',
	},
	'partiivi':{
		'minua':'mich',
		'sinua':'dich',
		'häntä':{
			'maskuliini':'ihn',
			'neutraali':'es',
			'feminiini':'sie',
		},
		'meitä':'uns',
		'teitä':'euch',
		'heitä':'sie',
		'Teitä':'Sie',
	},
	'genetiivi':{
		'minun':{
			'das':'mein',
			'der':'mein',
			'die':'meine',
			'monikko':'meine',
		},
		'sinun':{
			'das':'dein',
			'der':'dein',
			'die':'deine',
			'monikko':'deine',
		},
		'hänen':{
			'maskuliini':{
				'das':'sein',
				'der':'sein',
				'die':'seine',
				'monikko':'seine',
			},
			'neutraali':{
				'das':'sein',
				'der':'sein',
				'die':'seine',
				'monikko':'seine',
			},
			'feminiini':{
				'das':'ihr',
				'der':'ihr',
				'die':'ihre',
				'monikko':'ihre',
			}
		},
		'meidän':{
			'das':'unser',
			'der':'unser',
			'die':'unsere',
			'monikko':'unsere',
		},
		'teidän':{
			'das':'euer',
			'der':'euer',
			'die':'eure',
			'monikko':'eure',
		},
		'heidän':{
			'das':'ihr',
			'der':'ihr',
			'die':'ihre',
			'monikko':'ihre',
		},
		'Teidän':{
			'das':'Ihr',
			'der':'Ihr',
			'die':'Ihre',
			'monikko':'Ihre',
		},
	},
}

shuff(pronominit)
