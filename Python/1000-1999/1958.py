def main():
    num = float(input())
    numstr = str(num)
    c = 0

    if num >= 1 and num < 10:
        print('+%.4fE+00' %(num))
    
    elif num > 0 and num < 1:
        while 1 > num:
            c += 1
            num *= 10
        
        if c < 10:
            print('+%.4fE-0%i' %(num, c))
        else:
            print('+%.4fE-%i' %(num, c))

    elif num >= 10:
        while num >= 10:
            c += 1
            num = num/10

        if c < 10:
            print('+%.4fE+0%i' %(num, c))
        else:
            print('+%.4fE+%i' %(num, c))


    elif  num < -1 and -10 < num:
        print('-%.4fE+00' %(abs(num)))
    
    elif num < 0 and -1 < num:
        num = abs(num)

        while num < 1:
            c += 1
            num *= 10
        
        if c < 10:
            print('-%.4fE-0%i' %(num, c))
        else:
            print('-%.4fE-%i' %(num, c))
        
    elif num <= -10:
        num = abs(num)

        while num >= 10:
            c += 1
            num = num / 10
        
        if 10 > c:
            print('-%.4fE+0%i' %(num, c))
        else:
            print('-%.4fE+%i' %(num, c))
    
    elif num == 0.0:

        if numstr[0] == '-':
            print('%.4fE+00' %(num))
        else:
            print('+%.4fE+00' %(num))

main()