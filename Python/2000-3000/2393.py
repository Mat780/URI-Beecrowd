# -*- coding: utf-8 -*-

def main():
    cart = [ [ 0 for y in range(100) ] for x in range(100) ]
    v = int(input())
    soma = 0

    for c in range(v):
        lt = input().split()

        xi = int(lt[0])
        xf = int(lt[1])
        yi = int(lt[2])
        yf = int(lt[3])

        for x in range(xi, xf):
            for y in range(yi, yf):
                if cart[x][y] == 0:
                    cart[x][y] = 1
                    soma += 1
    
    print(soma)
        


main()