# -*- coding: utf-8 -*-

def main():
    n = int(input())
    anao = 0
    elfo = 0
    humanos = 0
    magos = 0
    xHobbits = 0


    for c in range(0, n):
        nome, raca = input().split()

        if raca == 'A':
            anao += 1
        elif raca == 'E':
            elfo += 1
        elif raca == 'H':
            humanos += 1
        elif raca == 'M':
            magos += 1
        elif raca == 'X':
            xHobbits += 1
        
    print('%i Hobbit(s)' %(xHobbits))
    print('%i Humano(s)' %(humanos))
    print('%i Elfo(s)' %(elfo))
    print('%i Anao(s)' %(anao))
    print('%i Mago(s)' %(magos))


main()