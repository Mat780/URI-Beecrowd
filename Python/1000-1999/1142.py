# -*- coding: utf-8 -*-

def main():
    x = 0
    y = 4
    vez = int(input())
    for c in range(0, vez*4):
        x += 1
        if x == y:
            y += 4
            print('PUM')
        else:
            print(x, end=' ')
main()

