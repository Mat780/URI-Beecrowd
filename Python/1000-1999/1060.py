# -*- coding: utf-8 -*-

def main():
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    n4 = float(input())
    n5 = float(input())
    n6 = float(input())
    tt = 0
    for c in (n1, n2, n3, n4, n5, n6):
        if c > 0:
            tt += 1
    
    print('%i valores positivos' %(tt))
main()