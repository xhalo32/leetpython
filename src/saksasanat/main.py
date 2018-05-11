#!/usr/bin/bash

import kurssi4kpl2, kurssi4kpl3, kurssi4kpl4
shuff = kurssi4kpl2.shuff

sanat = {**kurssi4kpl2.sanat,
        **kurssi4kpl3.sanat,
        **kurssi4kpl4.sanat}

import lolcat, learning, command
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
com = command.Command()#printer=lcat.print)

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
        lcat.print(learning.stats(sanat))

        lista = learning.shuff(sanat,n,t)
        llen = len(lista)
        last = None
        for i in range(len(lista)):
            word = lista[i][0]
            per = learning._get_per(learning.load()[word])
            while 1:
                if kieli == 'saksa':
                    k,v = lista[i]
                    lcat.print(f'{i+1}/{llen} '+
            'Mikä on {}{}{} ({:.0f}%) saksaksi? '.format(
                bcolors.UNDERLINE,k,bcolors.ENDC,100*per),0)
                    vastaus = input()
                elif kieli == 'suomi':
                    v,k = lista[i]
                    lcat.print(f'{i+1}/{llen} '+
            'Mikä on {}{}{} ({:.0f}%) suomeksi? '.format(
                bcolors.UNDERLINE,k,bcolors.ENDC,100*per),0)
                    vastaus = input()

                if com.parse(vastaus, last=last):
                    break

            correct = (vastaus == v)
            if correct:
                lcat.print('{}OKEIN{}'.format(bcolors.INVERTED,bcolors.ENDC))
            else:
                lcat.print('{}VÄÄRIN{} oikea on {}{}{}'.format(bcolors.INVERTED,bcolors.ENDC,bcolors.UNDERLINE,v,bcolors.ENDC))
            learning.saveword(word, correct, kieli)
            last = word

if __name__=='__main__': 
    try:
        main()
    except KeyboardInterrupt:
        print()
