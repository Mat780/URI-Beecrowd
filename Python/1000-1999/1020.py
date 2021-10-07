# -*- coding: utf-8 -*-

def main():
    d = int(input())
    y = d//365
    d %= 365
    m = d//30
    d %= 30
    print("%i ano(s)" %y)
    print("%i mes(es)" %m)
    print("%i dia(s)" %d)
main()