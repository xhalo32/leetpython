#!/usr/bin/bash

import kurssi4kpl2, kurssi4kpl3, kurssi4kpl4
shuff = kurssi4kpl2.shuff

sanat = {**kurssi4kpl2.sanat,
        **kurssi4kpl3.sanat,
        **kurssi4kpl4.sanat}

import lolcat, learning
learning.fillempty(sanat)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    INVERTED = '\033[7m'

def ins(string, before, after):
    return ''.join([before + x + after for x in string])

lcat = lolcat.Cat(saturation=0.7)

def main():
    while 1:
        lcat.print('Millä kielellä haluat vastata? ')
        kieli = input()
        assert kieli in ['saksa','suomi'], 'saksa|suomi'

        # lista = shuff(sanat)
        lcat.print(f'Montako sanaa? (max {len(list(sanat))}) ',0)
        n = int(input())
        lcat.print(f'Toistoja? [k/e] ',0)
        t = {"k": 1, "e": 0}[input()]

        lista = learning.shuff(sanat,n,t)
        llen = len(lista)
        for i in range(len(lista)):
            word = lista[i][0]
            if kieli == 'saksa':
                k,v = lista[i]
                lcat.print(f'{i}/{llen} '+'Mikä on {}{}{} saksaksi? '.format(bcolors.UNDERLINE,k,bcolors.ENDC),0)
                vastaus = input()
            elif kieli == 'suomi':
                v,k = lista[i]
                lcat.print(f'{i}/{llen} '+'Mikä on {}{}{} suomeksi? '.format(bcolors.UNDERLINE,k,bcolors.ENDC),0)
                vastaus = input()

            correct = (vastaus == v)
            if correct:
                lcat.print('{}OKEIN{}'.format(bcolors.INVERTED,bcolors.ENDC))
            else:
                lcat.print('{}VÄÄRIN{} oikea on {}'.format(bcolors.INVERTED,bcolors.ENDC,v))
            learning.saveword(word, correct, kieli)

if __name__=='__main__': 
    try:
        main()
    except KeyboardInterrupt:
        print()
