# -*- coding: utf-8 -*-

def main():
    n = int(input())
    fibonachi = [0, 1, 1, 2]
    

    for c in range(0, n):
        f = int(input())
        fib1 = 1
        fib2 = 1
        fib3 = 1

        if f <= 3:
            print('Fib(%i) = %i' %(f, fibonachi[f]))
        
        else:
            for c in range(2, f):
                fib1 = fib2
                fib2 = fib3
                fib3 = fib1 + fib2
            
            print('Fib(%i) = %i' %(f, fib3))


main()