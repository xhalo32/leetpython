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
        'saapua': 'an/kommen',
        'lentokentällä': 'am Flughafen',
        'raskaan reppunsa': 'seinen schweren Rucksack',
        'reppu': 'der Rucksack',
        'alkuiltapäivästä': 'am frühen Nachmittag',
        'erityisen': 'besonders',
        'melko': 'ziemlich',
        'tarkastus': 'die Kontrolle',
        'johonkin asti': 'bis zu',
        'lennon lähtö': 'der Abflug',
        'siksi': 'deswegen',
        'saksankielinen': 'deutschsprachig',
        'sanomalehti': 'die Zeitung',
        'lähtöportti': 'das Abfluggate',
        'tärkeä matsi': 'das wichtige Spiel',
        'matsi': 'das Spiel',
        'tulos': 'das Ergebnis',
        'olla hauskaa': 'Spaß machen',
        'ihminen': 'der Mensch',
        'pölöttää': 'an/quatschen',
        'sopiva, sopivasti': 'passend',
        'englanniksi': 'auf Englisch',
        'joitakin, muutama': 'ein paar',
        'kielikurssi': 'der Sprachkurs',
        'Yhdysvalloissa': 'in den USA',
        'useimmat asiat': 'die meisten Sachen',
        'käytännössä': 'in der Praxis',
        'liikemies': 'der Geschäftsmann',
        'ammatiltaan': 'vom Beruf',
        'puhumatta kieltä': 'ohne eine Sprache zu sprechen',
        'myydä': 'verkaufen',
        'maan kieli': 'die Landessprache',
        'tarkemmin sanottuna': 'genauer gesagt',
        'Amerikan länsirannikolla': 'an der amerikanischen Westküste',
        'rannikko': 'die Küste',
        'jatkuvasti': 'ständig',
        'tien päällä': 'auf Achse',
        'aksentti': 'der Akzent',
        'lentää': 'fliegen',
        'halpa': 'billig',
        'lento': 'der Flug',
        'sieltä': 'von dort',
        'uskomaton': 'unglaublich',
        'kaikkien aikojen paras elokuva': 'der beste Film aller Zeiten',
        'kauppa': 'der Laden',
        'esittää kysymyksiä': 'Fragen stellen',
        'kymmenittäin': 'Dutzende',
        'katsoa': 'schaun',
        'vastata': 'beantworten',
        'oman nimensä': 'seinen eigenen Namen',
        'kuulutus': 'die Durchsage',
        'välittömästi': 'dringend',
        'portti': 'Ausgang',
        'pyytää': 'bitten',
        'lukea': 'stehen auf',
        'vaihtaa': 'wechseln',
        'itse': 'selber',
        'olla valppaana': 'auf/passen',
        'lähteä matkaan': 'sich auf den Weg machen',
        'lähteä juoksemaan': 'los/rennen',
        'reilut 500 metriä': 'gut 500 Meter',
        'myöhäinen iltapäivä': 'der Spätnachmittag',
        'koko lentokenttä': 'der ganze Flughafen',
        'täynnä lentomatkustajia': 'voll von Fluggästen',
        'päästä eteenpäin': 'voran/kommen',
        'vaikea, raskas': 'schwer',
        'tavoitteessaan': 'an seinem Ziel',
        'lentokenttävirkailija': 'die Flughafenangestellte',
        'Hän on juuri sulkemassa lentoa': 'Sie ist gerade dabei, den Flug zu schließen',
        'sulkea': 'schließen',
        'puhutella jotakuta': 'an/sprechen',
        'onnenpekka': 'ein Glückskind',
        'odottaa': 'warten',
        'myöhästynyt': 'verspätet',
        'näin pitkään': 'so lange',
        'täsmällinen': 'pünktlich',
}
