# -*- coding: utf-8 -*-

def main():
    l1 = input().split(" ")
    a, b, c = l1
    a = int(l1[0])
    b = int(l1[1])
    c = int(l1[2])
    m1 = (a+b+abs(a-b))/2
    m2 = (m1+c+abs(m1-c))/2
    print ("%d eh o maior" %m2)
main()