def main():
    n = int(input())
    for c in range(1, n+1):
        num = int(input())
        if num == 0:
            print('NULL') 
        elif num % 2 == 0:
            print('EVEN', end=' ')
        else:
            print('ODD', end=' ')
        
        if num > 0:
            print('POSITIVE')
        elif num < 0:
            print('NEGATIVE')
main()