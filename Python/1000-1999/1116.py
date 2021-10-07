def main():
    vez = int(input())

    for c in range(0, vez):
        x, y = map(int, input().split())

        if y == 0:
            print('divisao impossivel')
        
        else:
            print('%.1f' %(x/y))
main()

