def main():
    num = float(input())

    for c in range(100):
        print("N[%i] = %.4f" %(c, num))
        num /= 2
main()