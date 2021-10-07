def main():
    l1 = []
    l2 = []
    for c in range(20):
        temp = int(input())
        l1.append(temp)
    l2 = l1[::-1]
    for c in range(20):
        print("N[%i] = %i" %(c, l2[c]))
        
main()