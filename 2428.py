# URI 2428 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 

def main():
    # Primeiro devemos pegar os 4 inputs e colocalos como inteiros
    A1, A2, A3, A4 = map(int,input().split())

    # Então faremos uma comparação para ver SE as areas são iguais
    # Pegando A1*A2 sendo a primeira area e A3*A4 sendo a segunda
    # Então comparamos para ver se elas são iguais, caso não sejam
    # Fazemos uma segunda comparação A1*A4 sendo a primeira area e
    # A3*A2 sendo a segunda area e vemos se são iguais.
    if A1*A2 == A3*A4 or A1*A4 == A3*A2:
        # Caso sejam iguais printar "S"
        print("S")
    else:
        # Caso não sejam iguais printar "N"
        print("N")

main()


# As informações da comparação eu tirei diretamente dos Inputs do exercicio

# 1 2 4 8
# 1*8 == 2*4 = "S"
# A1*A4 == A2*A3 = "S"

# 1 2 3 4
# 2*3 == 1*4 = "N"
# Não teria como ser válido pois não há como igualar

# 15 14 6 35
# 15*14 = 210  PS: Pode fazer as contas se tiver duvida
# 6*35 = 210
# 210 == 210 = "S"
# A1*A2 == A3*A4 = "S"

# Aprendam a saber extrair as informações dos inputs que o Uri dá
# Pois normalmente eles mesmo já dão dicas sobre o que deve ser feito