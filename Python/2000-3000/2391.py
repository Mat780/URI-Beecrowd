# -*- coding: utf-8 -*-

def main():

    x = int(input())
    pa = input().split()

    cont = 0
    seq = 0
    temp2 = 0
    Nseq = False

    for c in range(0, x):
        temp = int(pa[c])

        if Nseq:
            seq = temp - temp2
            Nseq = False

        elif seq != (temp-temp2):
            cont += 1
            Nseq = True


        temp2 = temp

    print(cont)


main()