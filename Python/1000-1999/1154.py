def main():
    x = 0
    cont = 0
    soma = 0

    while x >= 0:
        cont += 1
        soma += x
        x = int(input())
    
    print("%.2f" %(soma/(cont-1)))
main()