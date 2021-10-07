# -*- coding: utf-8 -*-

def main():
    l1 = []
    for c in range(0, 100):
        num = int(input())
        l1.append(num)

    n = sorted(l1, reverse=1)[0]

    print(n)
    print(l1.index(n)+1)
main()