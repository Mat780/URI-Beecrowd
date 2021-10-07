def main():
    for c in range(10):
        num = int(input())
        if num <= 0:
            print("X[%i] = 1" %(c))
        else:
            print("X[%i] = %i" %(c, num))
main()