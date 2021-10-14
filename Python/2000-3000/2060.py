# URI 2060 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 

def main():
    # Pegamos quantos numeros vão ter no vetor
    vezes = int(input())

    # Então pegamos o vetor de numeros
    vetor = input().split()

    # Definimos as variaveis com zero
    mult2 = mult3 = mult4 = mult5 = 0

    # Um laço que roda tantas vezes
    for c in range(vezes):
        # Definição de variavel com o valor transformado do vetor na posição c
        valorDoVetor = int(vetor[c])

        # Se o valorDoVetor divido por 2 der resto = 0, significa que ele é multiplo de 2
        if valorDoVetor % 2 == 0:
            # Adicionamos ao contador de mult2
            mult2 += 1
            
            # Caso ele seja divisivel por 2 ele talvez ele também seja divisivel por 4
            # Então fazemos essa verificação
            if valorDoVetor % 4 == 0:
                # Se ele for divisil por 4 então adicionamos ao contador mult4
                mult4 += 1
        
        # Se o valorDoVetor for multiplo de 3...
        if valorDoVetor % 3 == 0:
            # Adicionamos ao contador mult3
            mult3 += 1
        
        # Se o valorDoVetor for multiplo de 5...
        if valorDoVetor % 5 == 0:
            # Adicionamos ao contador mult5
            mult5 += 1
    
    # Printamos todos os valores com os prints adequados
    print("%d Multiplo(s) de 2" %( mult2 ) )
    print("%d Multiplo(s) de 3" %( mult3 ) )
    print("%d Multiplo(s) de 4" %( mult4 ) )
    print("%d Multiplo(s) de 5" %( mult5 ) )

main()