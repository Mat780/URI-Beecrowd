# -*- coding: utf-8 -*-

def main():
    n1, n2 = map(int, input().split())
    if n2 % n1 == 0 or n1 % n2 == 0:
        print("Sao Multiplos")
    else:
        print('Nao sao Multiplos')
main()