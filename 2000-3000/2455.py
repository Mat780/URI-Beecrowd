# URI 2455 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 

def main():
    E1, E2, D1, D2 = map(int, input().split())

    EsqTotal = E1 * E2
    DirTotal = D1 * D2

    if EsqTotal == DirTotal:
        print("0")
    
    elif EsqTotal > DirTotal:
        print("-1")
    
    else:
        print("1")

main()