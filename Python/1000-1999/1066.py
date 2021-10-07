# -*- coding: utf-8 -*-

def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())
    ttp = 0
    ttip = 0
    ttpos = 0
    ttneg = 0

    for c in (n1, n2, n3, n4, n5):
        if c % 2 == 0:
            ttp += 1
        elif c % 2 == 1:
            ttip += 1
        if c > 0:
            ttpos += 1
        elif c < 0:
            ttneg += 1
    
    print('%i valor(es) par(es)' %(ttp))
    print('%i valor(es) impar(es)' %(ttip))
    print('%i valor(es) positivo(s)' %(ttpos))
    print('%i valor(es) negativo(s)' %(ttneg))
main()
    