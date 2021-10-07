# -*- coding: utf-8 -*-

def main():
    x = int(input())
    while x != 0:
        for c in range(1, x):
            print(c, end=' ')
        if x == 1:
            print(x)
        else:
            print(c+1)
        
        x = int(input())
        
main()

