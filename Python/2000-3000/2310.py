# -*- coding: utf-8 -*-

def main():
    vez = int(input())
    totsaq = 0
    totcsaq = 0
    totbloq = 0
    totcbloq = 0
    totatk = 0
    totcatk = 0
    
    for c in range(0, vez):
        nome = input()
        tsaq, tbloq, tatk = map(int, input().split())
        csaq, cbloq, catk = map(int, input().split())

        totsaq += tsaq
        totcsaq += csaq

        totbloq += tbloq
        totcbloq += cbloq

        totatk += tatk
        totcatk += catk
    
    print('Pontos de Saque: %.2f %%.' %((totcsaq/totsaq)*100))
    print('Pontos de Bloqueio: %.2f %%.' %((totcbloq/totbloq)*100))
    print('Pontos de Ataque: %.2f %%.' %((totcatk/totatk)*100))

main()