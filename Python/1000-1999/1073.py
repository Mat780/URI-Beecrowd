def main():
    x = int(input())

    for c in range(1, x+1):
        temp = c**2
        if temp%2 == 0:
            print('%i^2 = %i' %(c, temp))
main()