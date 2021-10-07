def main():
    temp = int(input())
    temp2 = int(input())

    ini = min(temp, temp2)
    fim = max(temp, temp2)

    for c in range(ini+1, fim):
        if c%5 == 2 or c%5 == 3:
            print(c)

main()

