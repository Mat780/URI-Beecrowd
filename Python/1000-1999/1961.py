# -*- coding: utf-8 -*-

def main():
    p, cn = map(int, input().split())
    l1 = input().split()
    win = True
    pos = int(l1[0])

    for c in range(0, cn):
        temp = int(l1[c])

        if temp > pos+p or pos-p > temp:
            win = False
            break

        pos = temp

    if win:
        print('YOU WIN')
    
    else:
        print('GAME OVER')

main()