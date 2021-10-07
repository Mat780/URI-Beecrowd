# -*- coding: utf-8 -*-

def main():
    n = 0
    alc = 0
    gas = 0
    die = 0
    while n != 4:
        n = int(input())

        if n == 1:
            alc += 1
        elif n == 2:
            gas += 1
        elif n == 3:
            die += 1
    
    print('MUITO OBRIGADO')
    print('Alcool: %i' %(alc))
    print('Gasolina: %i' %(gas))
    print('Diesel: %i' %(die))


main()

