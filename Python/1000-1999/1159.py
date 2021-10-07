def main():
    while True:
        x = int(input())

        if x == 0:
            break

        soma = 0
        cont = 5
        while cont > 0:
            if x%2 == 0:
                soma += x
                cont -= 1
            x += 1
        print(soma)

main()