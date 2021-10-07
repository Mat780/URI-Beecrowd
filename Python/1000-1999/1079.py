# -*- coding: utf-8 -*-

def main():
    n = int(input())

    for c in range(0, n):
        n1, n2, n3 = map(float, input().split())

        med = (n1*2 + n2*3 + n3*5)/10
        print('%.1f' %(med))
main()