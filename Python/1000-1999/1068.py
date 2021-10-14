# URI 1068 em Python 3.9
# Programador: Matheus Felipe Alves Durães
# Não copie códigos, apenas leia-os e
# tente entender O QUE e POR QUE fazem o que fazem. 

def main():
    # Enquanto estiver VERDADEIRO rode...
    while True:
        # Tente fazer... (No caso ele vai tentar rodar o código, se ele não conseguir e der erro
        #                 esse erro será tratado no final do código)
        try:
            # Primeiro pegamos o input da expressão
            exp = input()
            # Então contabilizamos a quantidade de '(' e ')'
            esq = exp.count('(')
            dir = exp.count(')')

            # E colocamos uma variavel booleana para dizer se está certo ou não
            # Como o código começou ele ainda está certo
            certo = True

            # Se as variaveis esquerda e direita forem iguais
            # Ou seja se tiver a mesma quantidade de '(' e ')'
            if esq == dir:
                
                # Aqui ele verifica se o primeiro caractere é uma ')'
                # Se sim, então já não está mais correto essa expressão
                if exp[0] == ')':
                    certo = False
                
                # Aqui ele verifica se na ultima posição tem um '('
                # Se sim, então já não está mais correto essa expressão
                elif exp[-1] == '(':
                    certo = False
            
            # E caso esquerda e direita não sejam iguais significa que a expressão está errada
            else:
                certo = False
            
            # Se estiver certo
            if certo:
                print('correct')
            
            # Senão
            else:
                print('incorrect')

        # Caso o código de um erro de fim de arquivo ele não encerrará o código por completo
        # Ele vai entrar nessa excessão que definimos expecialmente para o erro de EOF
        except(EOFError):
            # Quando ele der esse erro ele vai executar o que estiver aqui abaixo
            # No caso com o break ele só irá parar o codigo mesmo
            # Porém esse tratamento de erro é necessário caso sua estrutura seja feita dessa forma
            # Pois o código finalizar por um erro/bug é diferente dele ser construido para tratar essas falhas
            # No nosso caso não há nada a ser feito depois do EOF por isso somente fechamos o programa
            break
main()