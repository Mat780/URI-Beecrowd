# URI 1238 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 

def main():
    # Primeiro pegamos a quantidade de inputs que teremos
    vezes = int(input())

    # Então entraremos no laço com o numero de vezes
    for c in range(vezes):
        # Definimos a primeira e segunda palavra
        palavra1, palavra2 = input().split()

        # Definimos de outras variaveis, como o tamanho das palavras e o contador
        texto_final = ''
        tamanho1 = len(palavra1)
        tamanho2 = len(palavra2)
        contador = 0

        # Enquanto o tamanho1 for maior que o contador E tamanho2 for maior que o contador rode...
        while tamanho1 > contador and tamanho2 > contador:
            # Texto final vai receber ele mesmo + (concatena) o caractere da palavra1 na posição do contador
            # E depois a mesma coisa porém com a palavra2 
            texto_final =  texto_final + palavra1[contador] + palavra2[contador]

            # Contador + 1 para avançar para a proxima posição
            contador += 1

            # Se o contador for maior ou igual que o tamanho1
            if contador >= tamanho1:
                # Signfica que a primeira palavra acabou por isso termine de puxar a palavra2
                texto_final = texto_final + palavra2[contador:]
            
            # Se o contador for maior ou igual que o tamanho2
            elif contador >= tamanho2:
                # Signfica que a segunda palavra acabou por isso termine de puxar a palavra1
                texto_final = texto_final + palavra1[contador:]

        # Por fim printamos o texto final
        print(texto_final)

main()