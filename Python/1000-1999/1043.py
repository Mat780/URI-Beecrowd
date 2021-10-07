# -*- coding: utf-8 -*-
def main():
    l1 = input().split(" ")
    z = float(l1[0])
    y = float(l1[1])
    x = float(l1[2])
    if abs(y-x)< z < (y+x) and (z-x)<y<(z+x) and (z - y)<x<(z+y):
        print("Perimetro = %.1f" %(x+y+z))
    else:
        r = (z + y) * x/2
        print("Area = %.1f" %r)
main()