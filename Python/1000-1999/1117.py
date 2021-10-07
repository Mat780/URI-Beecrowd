def main():
    x = 11
    while x > 10 or x < 0:
        x = float(input())

        if x > 10 or x < 0:
            print('nota invalida')
    
    y = 11
    while y > 10 or y < 0:
        y = float(input())

        if y > 10 or y < 0:
            print('nota invalida')   
    
    print('media = %.2f' %((x+y)/2))

main()

