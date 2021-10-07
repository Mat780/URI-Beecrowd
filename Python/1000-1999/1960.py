def main():
    x = int(input())

    num = ''

    if x == 1000:
        num += 'M'

    uni = x%10
    x = x//10
    dez = x%10
    x = x//10
    cent = x%10

    if cent > 0:

        if cent <= 3:
            num += 'C' * cent
        
        elif cent == 4:
            num += 'CD'

        elif cent == 5:
            num += 'D'

        elif cent > 5 and cent < 9:
            num += 'D' + 'C'* (cent-5)

        elif cent == 9:
            num += 'CM'
    

    if dez > 0:

        if dez <= 3:
            num += 'X'*dez

        elif dez == 4:
            num += 'XL'

        elif dez == 5:
            num += 'L'

        elif dez > 5 and dez < 9:
            num += 'L' + 'X'* (dez-5)

        elif dez == 9:
            num += 'XC'
    
    if uni > 0:

        if uni <= 3:
            num += 'I'*uni
        
        elif uni == 4:
            num += 'IV'

        elif uni == 5:
            num += 'V'

        elif uni > 5 and uni < 9:
            num += 'V' + 'I' * (uni-5)
        
        elif uni == 9:
            num += 'IX'

    print(num)

main()