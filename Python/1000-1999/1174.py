def main():
    for c in range(100):
        num = float(input())
        if num <= 10:
            print("A[%i] = %.1f" %(c, num))
main()