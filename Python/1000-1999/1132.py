# -*- coding: utf-8 -*-

def main():
    temp = int(input())
    temp2 = int(input())

    ini = min(temp, temp2)
    fim = max(temp, temp2)

    soma = 0

    for c in range(ini, fim+1):
        if c%13 != 0:
            soma += c
        
    print(soma)
main()

