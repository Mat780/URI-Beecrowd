# URI 1933 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 

def main():
    # Primeiro recebemos as cartas e seus valores
    carta1 , carta2 = map(int, input().split())

    # Em seguida pegamos o maior valor entre as duas;
    # Para isso poderiamos usar if e else ou a função max()
    maximo = max(carta1, carta2)

    # Depois que pegamos o maximo, nós o imprimimos
    print(maximo)

    # A execução desse exercicio não é complicada, mas o que realmente pega
    # nele é que o enunciado além de grande pode ser um tanto confuso quando
    # se lê só 1x , por isso tem que re-ler ele, porém isso gasta tempo
    # e cabeça, por isso tente focar nos pontos principais do exercicio

    # Neste por exemplo todo numero maior ganharia de um numero menor
    # Assim sendo precisamos do maior valor possivel do input, entendendo isso
    # A programação do codigo sai em 2 segs.
    # O problema é exatamente este: Entender o problema e o que ele quer
main()