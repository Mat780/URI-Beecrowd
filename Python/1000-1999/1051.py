# -*- coding: utf-8 -*-

def main():
    info1 = float(input())
    
    if info1 <= 2000.0:
        print('Isento')

    elif 2000.01 <= info1 <= 3000.0:
        print('R$ %.2f' %((info1-2000)*0.08))

    elif 3000.01 <= info1 <= 4500.0 :
        print('R$ %.2f' %(1000*0.08 + (info1-3000)*0.18))

    else:
        print('R$ %.2f' %(1000*0.08 + 1500*0.18+(info1-4500)*0.28))
    
main()