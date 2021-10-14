# URI 1632 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 

def main():
    # Primeiro pegamos a quantidade de inputs
    vezes = int(input())

    # Formamos um laço com o numero de vezes que ele precisará rodar
    for c in range(vezes):
        # Pegamos a palavra e colocamos todos os caracteres para maiusculo
        palavra = input().upper()

        # Definimos o contador como 1, para poder multiplicar depois
        cont = 1

        # Um laço para rodar cada caractere da palavra
        for caractere in (palavra): 

            # Se o caractere for igual a algum desses caracteres...
            if caractere in 'AEIOS':
                # cont *= 3 é igual a cont = cont * 3
                cont *= 3

            # Senão
            else:
                # cont *= 2 é igual a cont = cont * 2
                cont *= 2
        
        # Por fim printamos o numero do contador
        print(cont)

main()