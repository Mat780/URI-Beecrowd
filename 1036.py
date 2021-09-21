# URI 1036 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 

# DA biblioteca math IMPORTAR sqrt (raiz quadrada)
from math import sqrt 

def main():
    # Recebe os valores A B C para possivelmente formar um triangulo
    a, b, c = map(float, input().split())

    # Aqui calculamos a primeira parte do delta sem a raiz quadrada
    delta = b**2 - 4*a*c

    # Fazemos uma verificação simples se o delta é menor ou igual a 0
    # OU se A é igual a zero, pois se for também se torna impossivel calcular
    if delta <= 0 or a <= 0:
        print("Impossivel calcular")
    
    else:
        # Caso não seja impossivel de calcular então agora fazemos
        # a raiz quardade de delta
        delta = sqrt(delta)

        # Calculamos o R1 e o R2
        r1 = (-b + delta)/(2*a)
        r2 = (-b - delta)/(2*a)

        # Printando os dois resultados
        print("R1 = %.5f" %(r1) )
        print("R2 = %.5f" %(r2) )

main()