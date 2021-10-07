# -*- coding: utf-8 -*-

def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())
    tt = 0

    for c in (n1, n2, n3, n4, n5):
        if c % 2 == 0:
            tt += 1
    
    print('%i valores pares' %(tt))
main()
    