#!/usr/bin/python

import re

from aasia import aasia
from amerikat import amerikat
alue = amerikat

colorfmt = {
    'TEST' : '\033[38;2;200;255;200m',
    'RED' : '\033[91m',
    'GREEN' : '\033[92m',
    'END' : '\033[0m',
}
for i in range(16**3):
	colorfmt['x{:01X}{:01X}{:01X}'.format((i//256)%16,(i//16)%16,i%16)]='\033[38;2;{};{};{}m'.format(17*((i//256)%16),17*((i//16)%16),17*(i%16))

fmtcol = lambda text: text.format(**colorfmt)


def print_maat():
	for maa,pää in alue.items():
		print('{x2CF}{:12}   {x7F7}{}{END}'.format(maa,pää,**colorfmt))

def shuff(dictlist):
	l=len(dictlist)
	shuffled=[]
	while len(shuffled)<l:
		_sel=dictlist[randint(0,l-1)] # take random country
		sel=[_sel[0],_sel[1]['capital']] # turn it into a pair
		if sel in shuffled: continue # make sure no country is twice
		# more likely to add more difficult ones
		if random()*100<_sel[1]['difficulty']**2: shuffled.append(sel)
	return shuffled

from random import *
from time import sleep
def main():
	maksimi=10 # kuinka monta maata per kierros
	while 1:
		maat=shuff(list(alue.items()))
		pisteet=0
		maksimi=int(input("{x0AF}Montako kysymystä{END} (max {})? ".format(len(maat),**colorfmt)))
		if maksimi>len(maat): continue
		muoto=['maat','päät']['mp'.index(input("{x0CF}Maat vai pääkaupungit [m/p]{END}? ".format(**colorfmt)))]
		for maa,pää in maat[:maksimi]:
			if muoto=='päät':
				arvaus=input("{xF0F}Mikä on {} pääkaupunki{END}? ".format(maa,**colorfmt))
				if arvaus==pää:
					print("{x0F0}OIKEIN{END}".format(**colorfmt))
					pisteet+=1
				else: print("{xF00}VÄÄRIN{END} oikea oli {}".format(pää,**colorfmt))

			if muoto=='maat':
				arvaus=input("{xF0F}Minkä maan pääkaupunki on {}{END}? ".format(pää,**colorfmt))
				if arvaus==maa:
					print("{x0F0}OIKEIN{END}".format(**colorfmt))
					pisteet+=1
				else: print("{xF00}VÄÄRIN{END} oikea oli {}".format(maa,**colorfmt))

		print("{xFF0}Sait {}/{} oikein{END}".format(pisteet,maksimi,**colorfmt))

if __name__=='__main__': main()

