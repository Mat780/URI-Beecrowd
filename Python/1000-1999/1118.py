# -*- coding: utf-8 -*-

def main():
    while True:
        x = -1
        y = -1
        para = False

        while 0 > x or x > 10:
            x = float(input())
            if x < 0 or x > 10:
                print('nota invalida')
        
        while 0 > y or y > 10:
            y = float(input())
            if y < 0 or y > 10:
                print('nota invalida')
        
        media = (x + y)/2

        print('media = %.2f' %(media))

        while True:
            print('novo calculo (1-sim 2-nao)')
            dnv = int(input())
            if dnv == 1:
                break
            elif dnv == 2:
                para = True
                break
        
        if para:
            break

main()