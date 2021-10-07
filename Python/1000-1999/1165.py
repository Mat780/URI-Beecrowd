# -*- coding: utf-8 -*-

def main():
    n = int(input())


    for c in range(0, n):
        p = int(input())
        primo = True

        for i in range(2, p):
            if p/i == p//i:
                primo = False
        
        if primo:
            print('%i eh primo' %(p))
        
        else: 
            print('%i nao eh primo' %(p))

main()