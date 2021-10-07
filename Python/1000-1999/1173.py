def main():
    num = int(input())

    for c in range(10):
        print("N[%i] = %i" %(c, num))
        num *= 2
        
main()