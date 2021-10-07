def main():
    v = int(input())

    for c in range(0, v):
        i, f = map(int, input().split())
        let = ''

        for y in range(i, f+1):
            print(y, end='')
        for y in range(f, i-1, -1):
            y = str(y)
            for p in reversed(y):
                let = let + p
        
        print(let)


main()
