# -*- coding: utf-8 -*-

def main():
    l1 = input().split(" ")
    a, b, c = l1
    print("TRIANGULO: %.3f" % (float(a)*float(c)/2))
    print("CIRCULO: %.3f" % (3.14159 * float(c)**2))
    print("TRAPEZIO: %.3f" % ((float(a)+float(b))* float(c)/2))
    print("QUADRADO: %.3f" % (float(b)**2))
    print("RETANGULO: %.3f" % (float(a)*float(b)))
main()