# -*- coding: utf-8 -*-

def main():
    x, fim = map(int, input().split())
    cont = 0
    for c in range(1, fim+1):
        cont += 1
        if cont != x:
            print('%i' %(c), end=' ')
        else:
            cont = 0
            print('%i' %(c))
        
        
main()

