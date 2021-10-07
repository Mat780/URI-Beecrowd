# -*- coding: utf-8 -*-

def main():
    while True:
        x, y = map(int, input().split())
        
        if x > y:
            print('Decrescente')
        
        elif x < y:
            print('Crescente')

        else: # Se forem iguais
            break

main()