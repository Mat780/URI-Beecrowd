# URI 1038 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 


def mainSIMPLES():
    # Recebe o codigo da comida e a quantidade da mesma 
    codigo, qtde = map(int, input().split())

    # Aqui vamos começar a verificar o codigo e fazer
    # A quantidade vezes o valor da comida em questão
    if codigo == 1:
        qtde = qtde*4.00

    elif codigo == 2:
        qtde = qtde*4.50
    
    elif codigo == 3:
        qtde = qtde*5.00
    
    elif codigo == 4:
        qtde = qtde*2.00
    
    # Por mais que 5 seja o ultimo codigo possivel
    # É melhor especificar que só pode entrar se for 5
    # Do que simplesmente deixar com o else, isso é uma melhor prática
    elif codigo == 5:
        qtde = qtde*1.50
    
    # Por fim como sempre faremos o mesmo print só mudando o valor da variavel
    # Colocamos um print como esse no final do código, isto é melhor do que
    # colocar vários prints ao longo dos if/elifs e também é uma melhor prática
    print("Total: R$ %.2f" %(qtde) )

mainSIMPLES()

def mainEFICIENTE():
    # Recebe o codigo da comida e a quantidade da mesma 
    codigo, qtde = map(int, input().split())

    # Uma lista com os valores de cada comida
    lista_codigo = [4, 4.5, 5, 2, 1.5]

    # Agora fazemos a quantidade vezes o valor que pegamos na lista_codigo
    # Com o codigo-1 já que a lista começa no zero e não no 1
    qtde = qtde * lista_codigo[codigo-1]

    # Por fim printamos o resultado
    print("Total: R$ %.2f" %(qtde) )

mainEFICIENTE()