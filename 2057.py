# URI 2057 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 

def main():
    # Primeiro os horarios de saida, viagem e o fuso horário
    saida, viagem, fuso = map(int, input().split())

    # Juntamos todos os horários em uma só variavel
    hora_final = saida + viagem + fuso

    # Aqui temos uma condicional para verificar se passa da meia noite
    if hora_final >= 24:
        # Se passar da meia noite então reduzimos as 24 horas de um dia para
        # o outro dia
        hora_final = hora_final - 24

    # Caso ao invés de dar meia noite ele volte para a meia noite
    # Ou seja volte a ser menor que 0 então temos que adicionar um dia decorrido
    # Ou seja novamente 24 horas
    elif hora_final < 0:
        hora_final = hora_final + 24
    
    # Por fim imprimimos a hora final
    print(hora_final)

main()