# -*- coding: utf-8 -*-

def main():
    n = int(input())
    soma = 1

    for c in range(0, n):
        soma *= n
        n -= 1
    
    print(soma)

main()