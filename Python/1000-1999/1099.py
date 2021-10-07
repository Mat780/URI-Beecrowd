def main():
    n = int(input())
    c = 0

    for c in range(1 , n + 1):
        a, b = map(int, input().split())

        s = 0
        
        a = int(a) 
        b = int(b) 

        if a > b:
            for c in range(b+1, a):
                if c % 2 != 0:
                    s += c
        if a < b:
            for c in range(int(a)+1, int(b)):
                if c % 2 != 0:
                    s = s + c
        if a == b:
            s = 0
        print(s)
main()