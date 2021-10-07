def main():
    i, f = map(int, input().split())

    if i >= f:
        f += 24 - i
    
    elif i < f:
        f -= i
    
    print('O JOGO DUROU %i HORA(S)' %(f))

main()