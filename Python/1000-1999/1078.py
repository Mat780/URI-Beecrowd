# URI 1078 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 

def main():
    # Primeiro pegamos o numero inteiro para fazer a tabuada
    numero = int(input())

    # Depois definimos um laço de 1 até 11, pois o range só vai ir realmente até 10
    for c in range(1, 11):
        # Então pegamos e fazemos o resultado da multiplicação
        resultado = numero * c

        # E imprimimos o código do jeito que é pedido
        print("%i x %i = %i" %( c, numero, resultado ) )
    
    # Esse código é bem simples, mas ele expressa muito bem a questão dos laços e para que eles servem
    # Já que esse código feito sem o for, ficaria bem mais extenso e cansativo de ler e entender,
    # Porém com o for ele toma miseras 3 linhas, detalhe poderia ocupar até 2 somente porém dedici ficar com 3
    # Para que fosse mais didático.
main()