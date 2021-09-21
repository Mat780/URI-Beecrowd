# URI 1957 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 

def main():
    # Pegamos quantos produtos ele comprou
    qt_vezes = int(input())

    # Definimos o valor total primeiramente como zero, já que ainda
    # não temos nada, porém precisamos já declaralo para as futuras somas
    valor_total = 0

    # Agora faremos um laço definido com a quantidade de produtos que ele comprou
    for in range(qt_vezes):
        # Aqui pegamos tanto o código do produto quanto sua quantidade
        codigo, quantidade = map(int, input().split())

        # Então verificamos o codigo atráves de If e Elifs
        if codigo == 1001:
            # Após a verificação do codigo
            # O valor_total recebe a si mesmo + quantidade comprada vezes o valor
            # O valor muda a cada código já que é um produto diferente
            valor_total = valor_total + quantidade * 1.5

        elif codigo == 1002:
            valor_total = valor_total + quantidade * 2.5
        
        elif codigo == 1003:
            valor_total = valor_total + quantidade * 3.5
        
        elif codigo == 1004:
            valor_total = valor_total + quantidade * 4.5
        
        # Importante ressaltar como sempre, por mais que seja o ultimo codigo
        # É importante sim demarcar ele ou seja fazer a comparação certa ao invés de só colocar else
        # Pois em alguns casos só colocar o else pode levar a uma serie de erros
        # Esses erros aprenderemos a tratar bem mais pra frente então por hora...
        # Vamos evita-los :D
        elif codigo == 1005:
            valor_total = valor_total + quantidade * 5.5

    # Por fim imprimimos o resultado com 2 casas decimais
    # PS: %.2f é para imprimir um float com somente 2 casas decimais
    print("%.2f" %(valor_total) )

main()