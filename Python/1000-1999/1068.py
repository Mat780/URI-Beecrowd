# -*- coding: utf-8 -*-

def main():
    while True:
        try:
            exp = input()
            esq = exp.count('(')
            dir = exp.count(')')
            lista = []
            certo = True

            for c in exp:
                if c == '(' or c == ')':
                    lista.append(c)

            if esq == dir:
                
                if lista[0] == ')':
                    certo = False
                
                elif lista[-1] == '(':
                    certo = False
            
            else:
                certo = False
                
            if certo:
                print('correct')
            
            else:
                print('incorrect')

        except(EOFError):
            break
main()