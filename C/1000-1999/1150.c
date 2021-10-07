def main():
    x = int(input())
    y = 0
    soma = 0
    cont = 0

    while y <= x:
        y = int(input())
    
    while soma < y:
        soma += x
        cont += 1
        x += 1
    
    print("%i" %(cont))
main()