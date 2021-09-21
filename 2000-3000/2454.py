# URI 2428 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 

def main():
    # Primeiro nos pegamos os valores das duas portinhas
    S1, S2 = map(int, input().split())

    # Então comparamos pra ver se a primeira porta está em 0
    # Pois se ela estiver em 0 a resposta é imediatamente C
    if S1 == 0:
        print("C")
    else:
        # Caso a S1 esteja em 1 ela vai vir para cá
        # Então comparamos se a saída 2 está em 0
        if S2 == 0:
            # Se ela estiver então cairá em B
            print("B")
        else:
            # Senão irá cair em A
            print("A")

main()