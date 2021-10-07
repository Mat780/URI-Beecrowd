def main():
    num = int(input())
    l1 = list(map(int, input().split()))
    pos = 0
    men = l1[0]

    for c in range(num):
        if men > l1[c]:
            men = l1[c]
            pos = c
    
    print("Menor valor: %i" %(men))
    print("Posicao: %i" %(pos))

main()