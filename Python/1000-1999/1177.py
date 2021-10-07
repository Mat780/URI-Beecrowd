def main():
    num = int(input())
    cont = 0
    for c in range(1000):
        print("N[%i] = %i" %(c, cont))
        cont += 1
        if cont == num:
            cont = 0
main()