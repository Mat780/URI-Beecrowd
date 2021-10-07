def main():
    x = int(input())

    for c in range(1, 10001):
        if c%x == 2:
            print(c)
main()