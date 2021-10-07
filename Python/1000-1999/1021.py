# -*- coding: utf-8 -*-

def main():
    v = float(input())

    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

    print('NOTAS:')
    for nota in notas:
        qtd_nota = int(v / nota)
        print('{} nota(s) de R$ {:.2f}'.format(qtd_nota, nota))
        v -= qtd_nota * nota

    print('MOEDAS:')
    for moeda in moedas:
        qtd_moedas = int(round(v,2) / moeda)
        print('{} moeda(s) de R$ {:.2f}'.format(qtd_moedas, moeda))
        v -= qtd_moedas * moeda
main()