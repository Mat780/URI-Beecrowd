# -*- coding: utf-8 -*-

def main():
    x = int(input())

    for c in range(0, x):
        certo = True
        alt, esp, gal = map(int, input().split())

        if alt < 200:
            certo = False 

        elif alt > 300:
            certo = False
        
        if esp < 50:
            certo = False
        
        if gal < 150:
            certo = False
        
        if certo:
            print('Sim')
        else:
            print('Nao')


main()
