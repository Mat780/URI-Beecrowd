# -*- coding: utf-8 -*-

def main():

    x = int(input())

    for c in range(0, x):

        val = input().upper()

        val = val + 'A'

        soma = 0
        temp = '0'

        for i in (val):
            if i.isnumeric():
                temp = temp + i

            else:
                soma += int(temp)
                temp = '0'
            
        
        print(soma)


main()