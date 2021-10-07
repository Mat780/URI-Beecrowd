# -*- coding: utf-8 -*-

def main():
    while True:
        x, y = map(int, input().split())
        soma = 0

        if x <= 0 or y <= 0:
            break

        temp = x
        temp2 = y

        x = max(temp, temp2)
        y = min(temp, temp2)

        for c in range(y, x+1):
            print('%i' %(c), end=' ')
            soma += c
        
        print('Sum=%i' %(soma))

main()