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
    'erään paikallislehden haastattelussa' : 'in Interview mit einer Lokalzeitung',
    'kertoa' : 'berichten',
    'parhaimmat' : 'die besten',
    'huonoimmat' : 'die schlechtesten',
    'kokemus' : 'die Erfahrung',
    'suhteiden avulla' : 'durch Beziehungen',
    'suhde' : 'die Beziehung',
    'omistaja' : 'der Besitzer',
    'hän tarvitsi' : 'er brauchte',
    'apulainen' : 'die Hilfskraft',
    'tarjoilija' : 'der Kellner',
    'putsata' : 'putzen',
    'joskus' : 'manchmal',
    'eteistila' : 'die Vorhalle',
    'puutarha' : 'der Garten',
    'uima-allas' : 'der Pool',
    'kieli' : 'die Sprache',
    'keskustella' : 'sich unterhalten mit',
    'useita' : 'mehrere',
    'lähes joka päivä' : 'fast jeden Tag',
    'aurinkotuoli' : 'der Liegestuhl',
    'auringossa' : 'in der Sonne',
    'monia muita' : 'viele andere',
    'kielletty' : 'verboten',
    'kieltää' : 'verbieten',
    'esiintyä' : 'vor/kommen',
    'pakata' : 'ein/packen',
    'vapaa-aika' : 'die Freizeit',
    'noin' : 'rund',
    'viikossa' : 'in der Woche',
    'minun pisin työpäiväni' : 'mein längster Arbeitstag',
    'työpäivä' : 'der Arbeitstag',
    'vähintään' : 'mindestens',
    'yleensä' : 'meistens',
    'kaupunkiin' : 'in die Stadt',
    'lauluteksti' : 'der Liedtext',
    'ulkona' : 'draußen',
    'vaikuttaa joltakin' : 'scheinen',
    'suositella' : 'empfehlen',
    'täytyy tehdä töitä' : 'man muss arbeiten',
    'kovasti' : 'hart',
    'kaikkea mahdollista' : 'alles Mögliche',
    'mahdollinen' : 'möglich',
    'sukeltaminen' : 'das Tauchen',
    'vaeltaminen' : 'das Wandern',
    'juhliminen' : 'das Feiern',
    'rentoutua' : 'sich entspannen',
    'itse asiassa' : 'eigentlich',
}
