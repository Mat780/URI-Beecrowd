# -*- coding: utf-8 -*-

def main():
    n = float(input())

    if n < 400.01:
        prt = n * 0.15
        print('Novo salario: %.2f' %(n + prt))
        print('Reajuste ganho: %.2f' %(prt))
        print('Em percentual: %i %%' %(15) )
    elif n < 800.01:
        prt = n * 0.12
        print('Novo salario: %.2f' %(n + prt))
        print('Reajuste ganho: %.2f' %(prt))
        print('Em percentual: %i %%' %(12))
    elif n < 1200.01:
        prt = n * 0.10
        print('Novo salario: %.2f' %(n + prt))
        print('Reajuste ganho: %.2f' %(prt))
        print('Em percentual: %i %%' %(10))
    elif n <= 2000.0:
        prt = n * 0.07
        print('Novo salario: %.2f' %(n + prt))
        print('Reajuste ganho: %.2f' %(prt))
        print('Em percentual: %i %%' %(7))
    else:
        prt = n * 0.04
        print('Novo salario: %.2f' %(n + prt))
        print('Reajuste ganho: %.2f' %(prt))
        print('Em percentual: %i %%' %(4))
main()