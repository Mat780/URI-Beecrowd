# -*- coding: utf-8 -*-

def main():
    x, y, z = map(int, input().split())

    maior = max(x, y, z)
    menor = min(x, y, z)
    
    if x == maior:
        if y > z:
            meio = y
        elif y < z:
            meio = z
        elif y == z:
            meio = y
    elif y == maior:
        if x > z:
            meio = x
        elif x < z:
            meio = z
        elif x == z:
            meio = z
    elif z == maior:
        if x > y:
            meio = z
        elif x < y:
            meio = y
        elif x == y:
            meio = y

    if maior < meio + menor and meio - menor < maior:
        print('Valido-', end='')

        if maior == meio == menor:
            print('Equilatero')
        
        elif meio == menor or maior == meio:
            print('Isoceles')
        
        elif maior != meio != menor:
            print('Escaleno')
        
        if maior**2 == menor**2 + meio**2:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
    
    else:
        print('Invalido')


    

main()