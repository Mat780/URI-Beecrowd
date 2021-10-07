# -*- coding: utf-8 -*-

def main():
    z1, x1, y1 = map(int, input().split())
    z2, x2, y2 = map(int, input().split())

    zf = 0
    xf = 0
    yf = 0

    if z1 == z2:
        zf = 1

    else:    
        for c in range(z1, z2+1, z1):
            zf += 1
    
    if x1 == x2:
        xf = 1
    
    else:
        for c in range(x1, x2+1, x1):
            xf += 1


    if y1 == y2:
        yf = 1
    

    else:
        for c in range(y1, y2+1, y1):
            yf += 1
    
    print(zf*xf*yf)


main()