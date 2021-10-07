def main():
    cont = int(input())
    num = 0
    aux = 0

    fib = 3
    fib2 = 5
    auxFib = fib + fib2

    while cont > 0:
        temp = fib2 - fib-1
        if temp != 0:
            aux = cont
            cont -= temp
        if cont == 0:
            num = fib2-1
        elif cont < 0:
            num = fib+aux
        fib = fib2
        fib2 = auxFib
        auxFib = fib + fib2

    
    print(num)
 
main()