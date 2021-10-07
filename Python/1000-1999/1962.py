# -*- coding: utf-8 -*-

def main():
    vez = int(input())
    att = 2015

    for c in range(0, vez):

        anos = int(input())

        temp = att - anos

        if temp > 0:
            print('%i D.C.' %(temp))

        if temp <= 0:
            temp = (temp-1)*-1
            print('%i A.C.' %(temp))
main()