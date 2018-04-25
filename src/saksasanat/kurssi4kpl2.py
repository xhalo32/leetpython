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
        'lomamökki': 'die Ferienhütte',
        'lähellä jotakin': 'in der Nähe von',
        'suomalaiset tavat': 'die finnischen Sitten',
        'täysin siemauksin': 'in vollen Zügen',
        'sitä vastoin': 'hingegen',
        'mökki': 'die Hütte',
        'mieluiten': 'am liebsten',
        'joka paikasta': 'überall',
        'kutittaa': 'jucken',
        'hyttynen': 'die Mücke',
        'tosi, oikea': 'richtig',
        'vessa': 'das Klo',
        'ulkovessa': 'das Plumpsklo',
        'tosi ällöttävä': 'richtig ekelhaft',
        'hyi': 'igitt',
        'joka tapauksessa': 'sowieso',
        'mennä saunaan': 'in die Sauna gehen',
        'poimia marjoja': 'Beeren pflücken',
        'valita': 'aus/suchen',
        'juuri': 'gerade',
        'nyt on sinun vuorosi': 'jetzt bist du dran',
        'ihan liian kuuma': 'viel zu heiß',
        'no sitten': 'na dann',
        'hikoilla': 'schwitzen',
        'välillä': 'zwischendurch mal',
        'löyly': 'der Aufguss',
        'järveen': 'rein in den See',
        'meille alkaa tämä erämaa pikkuhiljaa rittää':
            'wir haben langsam genug von dieser Wildnis hier',
        'erämaa': 'die Wildnis',
        'susi, sudet': 'der Wolf, Wölfe',
        'rakas': 'der Liebling',
        'haluan pois täältä': 'ich will hier weg',
        'kaupunkilapsi': 'das Stadtkind',
        'keskellä luontoa': 'mitten in der Natur',
        'te halusitte': 'ihr wolltet',
        'vuorten lapsi': 'Kind der Berge',
        'romantiikka': 'die Romantik',
        'karhu, karhut': 'der Bär, Bären',
        'vuokra-auto': 'der Mietwagen',
        'aste': 'das Grad',
        'avautua': 'auf/gehen',
        'nopein askelin': 'mit schnellem Schritt',
        'askel': 'der Schritt',
        'järven suuntaan': 'Richtung See',
        'suunta': 'die Richtung',
        'paksu': 'dick',
        'jääkerros': 'die Eisschicht',
        'pumpun avulla': 'dank einer Pumpe',
        'kohta, paikka': 'die Stelle',
        'epäröimättä': 'ohne zu zögern',
        'he laskeutuvat tikkaita pitkin alas': 'sie steigen die Leiter hinunter',
        'laskeutua, nousta': 'steigen',
        'tikkaat': 'steigedie Leiter',
        'jääkylmä': 'eiskalt',
        'muutaman kerran': 'ein paarmal',
        'edestakaisin': 'hin und her',
        'tämän jälkeen': 'danach',
        'nopeasti': 'rasch',
        'hullu': 'wahnsinnig',
        'kuulostaa': 'klingen',
        'julkinen': 'öffentlich',
        'laituri': 'der Steg',
        'reikä': 'das Loch',
        'säännöllinen': 'regelmäßig',
        'terveys': 'die Gesundheit',
        'alussa': 'am Anfang',
        'varovainen': 'vorsichtig',
        'hiestä märkänä': 'verschwitzt',
        'suoraan': 'direkt',
        'avanto': 'das Eisloch',
        'hypätä': 'springen',
}
