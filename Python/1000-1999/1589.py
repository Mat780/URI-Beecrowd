# -*- coding: utf-8 -*-

def main():
    n = int(input())

    for c in range(0, n):
        n1, n2 = map(int, input().split())

        print(n1 + n2)

main()