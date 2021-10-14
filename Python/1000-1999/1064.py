# URI 1064 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 

def main():
    # Definimos 2 variaveis com 0 para iniciar nossa contagem
    valores_positivos = 0
    media = 0
    
    # Em sequencia fazemos um laço que se repete 6x
    for c in range(6):
        # Dentro do laço pegamos o numero do input float e colocamos em uma variavel
        numero = float(input())

        # E então fazemos a comparação para saber se ele é um numero positivo
        if numero > 0:
            # Se ele for um numero positivo então ele é adicionado aos valores positivos
            # Além de ser adicionado a variavel média para ser feita a média aritmética depois
            valores_positivos += 1
            media += numero

    # Após a conclusão do laço fazemos a média aritmética com os valores que pegamos
    media /= valores_positivos

    # Por fim printamos os valores como foram requisitados
    print('%i valores positivos' %(valores_positivos))
    print('%.1f' %(media))
main()