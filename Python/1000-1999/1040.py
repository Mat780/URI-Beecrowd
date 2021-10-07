def main():
    n1, n2, n3, n4 = map(float, input().split())

    m = (n1*2 + n2*3 + n3*4 + n4)/10

    print('Media: %.1f' %(m))
    
    if m >= 7:
        print('Aluno aprovado.')
    
    elif m < 6.9 and m >= 5.0:
        print('Aluno em exame.')
        ex = float(input())
        print('Nota do exame: %.1f' %(ex))

        m = (m+ex)/2

        if m >= 5:
            print('Aluno aprovado.')
            print('Media final: %.1f' %(m))
        
        else:
            print('Aluno reprovado.')

    else:
        print('Aluno reprovado.')


main()