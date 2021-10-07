# -*- coding: utf-8 -*-


def main():
    l1 = input().split(" ")
    a = float(l1[0])
    b = float(l1[1])
    c = float(l1[2])
    n1 = 0
    n2 = 0
    n3 = 0
    if a >= b and a >= c:
        n1 = a
        if b >= c:
            n2 = b
            n3 = c
        else:
            n2 = c
            n3 = b
    if b >= a and b >= c:
        n1 = b
        if a >= c:
            n2 = a
            n3 = c
        else:
            n2 = c
            n3 = a
    if c >= a and c >= b:
        n1 = c
        if a >= b:
            n2 = a
            n3 = b
        else:
            n2 = b
            n3 = a
    a = n1
    b = n2
    c = n3
    if a >= (b+c):
        print("NAO FORMA TRIANGULO")
    else:
        if a**2 == b**2 + c**2:
            print("TRIANGULO RETANGULO")
        if a**2 > b**2 + c**2:
            print("TRIANGULO OBTUSANGULO")
        if a**2 < b**2 + c**2:
            print("TRIANGULO ACUTANGULO")
        if a == b == c:
            print("TRIANGULO EQUILATERO")
        if a == b != c or a != b == c or b != a == c:
            print("TRIANGULO ISOSCELES") 
main()