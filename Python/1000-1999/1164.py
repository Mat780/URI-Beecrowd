# -*- coding: utf-8 -*-

def main():
    n = int(input())

    for c in range(0, n):
        n1 = int(input())
        soma = 0

        for i in range(1, n1):
            if n1/i == n1//i:
                soma += i
        
        if soma == n1:
            print('%i eh perfeito' %(n1))
        
        else:
            print('%i nao eh perfeito' %(n1))

main()