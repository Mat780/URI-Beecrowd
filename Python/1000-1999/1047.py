# -*- coding: utf-8 -*-

def main():
    l1 = input().split()
    hi = int(l1[0])
    mi = int(l1[1])
    hf = int(l1[2])
    mf = int(l1[3])

    minuto = 60
    hrmin = 3600
    dia = hrmin*24

    si = (hi*hrmin)+(mi*minuto)
    sf = (hf*hrmin)+(mf*minuto)

    if sf > si:
        sf -= si
        hf = sf//hrmin
        sf -= hf * hrmin
        mf = sf//minuto
        print('O JOGO DUROU %i HORA(S) E %i MINUTO(S)' %(hf, mf))
    else:
        sf += dia
        sf -= si
        hf = sf//hrmin
        sf -= hf * hrmin
        mf = sf//minuto
        print('O JOGO DUROU %i HORA(S) E %i MINUTO(S)' %(hf, mf))

main()