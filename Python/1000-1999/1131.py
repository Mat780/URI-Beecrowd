def main():
    gremio = 0
    inter = 0
    emp = 0
    jog = 0
    while True:
        i, g = map(int,input().split())
        jog += 1
        if i == g:
            emp += 1
        elif i > g:
            inter += 1
        else:
            gremio += 1
        
        print('Novo grenal (1-sim 2-nao)')
        res = int(input())

        if res == 2:
            break
    
    print('%i grenais' %(jog))
    print('Inter:%i' %(inter))
    print('Gremio:%i' %(gremio))
    print('Empates:%i' %(emp))

    if inter > gremio:
        print('Inter venceu mais')
    
    elif gremio > inter:
        print('Gremio venceu mais')
    
    else:
        print('Nao houve vencedor')


main()

