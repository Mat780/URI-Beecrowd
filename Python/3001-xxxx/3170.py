# -*- coding: utf-8 -*-

def main():
    b = int(input())
    g = int(input())

    g = g // 2

    if b >= g:
        print("Amelia tem todas bolinhas!")
    else:
        print('Faltam %i bolinha(s)' %(g-b))

main()