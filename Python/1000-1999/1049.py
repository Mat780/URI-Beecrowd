# -*- coding: utf-8 -*-

def main():
    info1 = input().lower()
    info2 = input().lower()
    info3 = input().lower()

    if info1 == 'vertebrado':
        if info2 == 'ave':
            if info3 == 'carnivoro':
                print('aguia')
            elif info3 == 'onivoro':
                print('pomba')
        elif info2 == 'mamifero':
            if info3 == 'onivoro':
                print('homem')
            elif info3 == 'herbivoro':
                print('vaca')
    elif info1 == 'invertebrado':
        if info2 == 'inseto':
            if info3 == 'hematofago':
                print('pulga')
            elif info3 == 'herbivoro':
                print('lagarta')
        elif info2 == 'anelideo':
            if info3 == 'hematofago':
                print('sanguessuga')
            elif info3 == 'onivoro':
                print('minhoca')
main()