# URI 1009 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 

def main():
    # Variavel nome recebe uma string do nome da pessoa
    nome = input()

    # Variavel salario_fixo recebe um valor float do salario fixo
    salario_fixo = float(input()) 

    # Variavel vendas recebe um valor float das vendas dele
    vendas = float(input())

    # Salario final é a soma do salario fixo com 15% das vendas
    salario_final = salario_fixo + (vendas * 0.15)

    # Imprimindo os resultados 
    # PS: %.2f para imprimir somente 2 casas decimais do float
    print("TOTAL = R$ %.2f" %(salario_final) )

main()