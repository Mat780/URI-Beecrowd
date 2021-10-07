def main():
    vez = int(input())
    
    for c in range(vez):
        x, y = map(int, input().split())
        soma = 0
        while y > 0:
            if x%2 == 1:
                y -= 1
                soma += x
            x += 1
        print(soma)

main()