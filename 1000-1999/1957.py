# URI 1957 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 

def main():
    # Primeiro recebemos o numero inteiro
    numero = int(input())

    # Em seguida o transformamos o inteiro em hexadecimal
    hexadecimal = hex(numero)

    # Aqui precisamos tirar o 0x... pois eles não fazem parte do nosso print
    hexadecimal = hexadecimal[2:]

    # E por fim nos temos que colocar tudo em maiúsculo, como está no output
    hexadecimal = hexadecimal.upper()

    # Como são 3 passos na mesma variavel poderiamos simplificar em 1 só linha
    # Porém decidi deixar separado para melhor compreensão, mas caso fosse feito
    # Tudo junto, a linha ficaria como está abaixo

    #hexadecimal = hex(numero)[2:].upper()

    # Assim printamos a variavel hexadecimal e terminamos o código
    print(hexadecimal)

main()