# -*- coding: utf-8 -*-

def main():
    vez = int(input())
    
    for c in range(0, vez):
        nome = input()
        dif = float(input())
        l2 = input().split()

        maior = 0
        menor = 11
        tot = 0

        for c in range(0, 7):
            temp = float(l2[c])

            tot += temp

            if temp > maior:
                maior = temp
            if temp < menor:
                menor = temp
        
        tot -= maior + menor
        tot *= dif

        print('%s %.2f' %(nome, tot))


main()