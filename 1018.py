# URI 1018 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 

def mainSIMPLES():
    # Variavel dinheiro recebe o valor inteiro a ser processado
    dinheiro = int(input())

    # Imprimos o valor conforme o exercicio pede
    print(dinheiro)

    # Variavel temporaria para pegar o troco baseado na divisão inteira
    # da variavel dinheiro pela nota que queremos de troco
    temp = dinheiro//100

    # Em sequencia precismos reduzir do montante de dinheiro o troco que pegamos
    dinheiro = dinheiro - (temp*100)

    # E então imprimimos o troco
    print("%i nota(s) de R$ 100,00" %(temp) )

    # Agora repetimos o mesmo passo somente alterando os valores
    # Por isso vou condensar e deixar agrupado por montante

    # Para o troco de R$50.00
    temp = dinheiro//50
    dinheiro = dinheiro - (temp*50)
    print("%i nota(s) de R$ 50,00" %(temp) )

    # Para o troco de R$20.00
    temp = dinheiro//20
    dinheiro = dinheiro - (temp*20)
    print("%i nota(s) de R$ 20,00" %(temp) )

    # Para o troco de R$10.00
    temp = dinheiro//10
    dinheiro = dinheiro - (temp*10)
    print("%i nota(s) de R$ 10,00" %(temp) )

    # Para o troco de R$5.00
    temp = dinheiro//5
    dinheiro = dinheiro - (temp*5)
    print("%i nota(s) de R$ 5,00" %(temp) )

    # Para o troco de R$2.00
    temp = dinheiro//2
    dinheiro = dinheiro - (temp*2)
    print("%i nota(s) de R$ 2,00" %(temp) )

    # Para o troco de R$1.00 é somente printar o resultado final
    print("%i nota(s) de R$ 1,00" %(dinheiro) )

mainSIMPLES()

# Abaixo está uma solução um pouco mais complexa porém mais eficaz
# A solução abaixo contêm LISTA e FOR

def mainFOR():
    # Variavel dinheiro recebe o valor inteiro a ser processado
    dinheiro = int(input())

    # Lista com os valores que usaremos no for para os calculos
    lista_de_valores = [100, 50, 20, 10, 5, 2, 1]

    # Imprimos o valor conforme o exercicio pede
    print(dinheiro)

    for c in range(7):
        # Primeiro pegamos o valor do vetor para calcular o restante
        valor = lista_de_valores[c]

        # Após pegarmos o valor fazemos o calculo, assim como faziamos na forma simples
        temp = dinheiro//valor

        # Em seguida diminuimos do montante de dinheiro 
        dinheiro = dinheiro - (temp * valor)

        # Então printamos o resultado, juntamente ao valor do vetor
        # baseado no iteravel do for ou seja o "c"
        print("%i nota(s) de R$ %i,00" %(temp, valor) )

mainFOR()