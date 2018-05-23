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
        'päntätä': 'pauken',
        'ensi viikolla': 'nächste Woche',
        'päättökoe': 'die Abschlussprüfung',
        'ylioppilastutkinto': 'die Matura',
        'tuskin': 'kaum',
        'ankara': 'streng',
        'tehdä asia hänelle helpommaksi': 'ihn die Sache leichter machen',
        'nousisitko sängystä': 'würdest du aufstehen',
        'opiskella': 'lernen',
        'muuten jäät luokalle': 'sonst bleibst du noch sitzen',
        'nytkö jo': 'jetzt schon',
        'jäädä väliin': 'verpassen',
        'lounas': 'das Mittagessen',
        'yrittää': 'versuchen',
        'keskittyä': 'sich konzentrieren',
        'uneksia': 'träumen von',
        'koulun päättymisen jälkeen': 'nach dem Abschluss',
        'päättyminen': 'der Abschluss',
        'koko kesän': 'den ganzen Sommer',
        'etelässä': 'im Süden',
        'viettää': 'verbringen',
        'harkita': 'überlegen',
        'lämpöön': 'in die Wärme',
        'tai jotain': 'oder so',
        'etkö tekisi yhtään töitä': 'würdest du gar nicht arbeiten',
        'en oikeastaan': 'eigentlich nicht',
        'sinun pitäisi': 'du solltest',
        'omaa rahaa': 'eigenes Geld',
        'ansaita': 'verdienen',
        'maksaa': 'bezahlen',
        'etsiä': 'suchen',
        'kesätyö': 'der Ferienjob',
        'mahdoton': 'unmöglich',
        'työkaveri': 'der Arbeitskollege',
        'Mallorcalla': 'auf Mallorca',
        'johtaa': 'führen',
        'ihanko totta?': 'echt?',
        'etelään': 'in den Süden',
        'olisi': 'wäre',
        'päästä läpi': 'bestehen',
        'yritän parhaani': 'ich gebe mein Bestes',
}
