def main():
    vez = int(input())

    fib = 0
    fib2 = 1
    aux = 0

    for c in range(vez):
        if c == vez-1:
            print("%i" %(aux))
        else:
            print("%i" %(aux), end=' ')
        fib = fib2
        fib2 = aux
        aux = fib + fib2 
main()