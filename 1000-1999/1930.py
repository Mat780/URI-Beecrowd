# URI 1930 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 

def main():
    # Primeiramente pegamos todos os inputs
    t1, t2, t3, t4 = map(int, input().split())

    # Depois somamos todos os valores, como são tomadas cada extensão tem
    # que se conectar na outra, assim a T2 conecta na T1 , a T3 conecta na T2
    # e por fim a T4 conecta na T3 , então assim perdemos 3 tomadas das extensões
    # Por isso reduzimos do total 3
    qtde_final = t1 + t2 + t3 + t4 - 3

    # Por fim printamos o resultado final
    print(qtde_final)

main()