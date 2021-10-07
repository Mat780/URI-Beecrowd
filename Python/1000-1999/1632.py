# -*- coding: utf-8 -*-

def main():
    v = int(input())

    for c in range(0, v):
        
        x = input().upper()
        cont = 1


        for i in (x): 

            if i in 'AEIOS':
                cont *= 3
            
            else:
                cont *= 2
        
        print(cont)


main()