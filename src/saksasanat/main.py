#!/usr/bin/bash

import kurssi4kpl1
sanat = kurssi4kpl1.sanat
shuff = kurssi4kpl1.shuff

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def ins(string, before, after):
    return ''.join([before + x + after for x in string])

def main():
	while 1:
		kieli = input('Millä kielellä haluat vastata? ')
		assert kieli in ['saksa','suomi'], 'saksa|suomi'
		
		lista = shuff(sanat)
		for i in range(len(lista)):
			if kieli == 'saksa':
				k,v = lista[i]
				vastaus = input('Mikä on {} saksaksi? '.format(ins(k,bcolors.BOLD,bcolors.ENDC)))
			elif kieli == 'suomi':
				v,k = lista[i]
				vastaus = input('Mikä on {} suomeksi? '.format(ins(k,bcolors.BOLD,bcolors.ENDC)))

			if vastaus == v:
				print('OKEIN')
			else:
				print('VÄÄRIN oikea on {}'.format(v))

if __name__=='__main__': 
	try:
		main()
	except KeyboardInterrupt:
		print()
