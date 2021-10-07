# -*- coding: utf-8 -*-

def main():
    n = int(input())
    coe = 0
    rato = 0
    sap = 0
    cob = 0

    for c in range(0, n):
        l1 = input().split()
        temp = int(l1[0])

        if l1[1] == 'C':
            coe += temp
            cob += temp
            
        elif l1[1] == 'R':
            rato += temp
            cob += temp

        elif l1[1] == 'S':
            sap += temp
            cob += temp
    
    print('Total: %i cobaias' %(cob))
    print('Total de coelhos: %i' %(coe))
    print('Total de ratos: %i' %(rato))
    print('Total de sapos: %i' %(sap))
    print('Percentual de coelhos: %.2f %%' %( (coe/cob)*100 ))
    print('Percentual de ratos: %.2f %%' %( (rato/cob)*100 ))
    print('Percentual de sapos: %.2f %%' %( (sap/cob)*100 ))

main()