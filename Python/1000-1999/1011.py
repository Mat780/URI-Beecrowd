# URI 1011 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 

def main():
    # Variavel raio recebe um numero inteiro referente ao raio
    raio = int(input())

    # Valor de pi dado pelo exercicio
    pi = 3.14159

    # Volume é calculado por 4/3 vezes pi vezes raio ao cubo
    volume = (4/3) * pi * raio**3

    # Imprimindo o volume
    # PS: %.3f para imprimir um valor float com 3 casas decimais
    print("VOLUME = %.3f" %(volume) )

main()