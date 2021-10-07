def main():
    x = int(input())
    den = 0
    fora = 0
    for c in range(0, x):
        y = int(input())

        if 10 <= y and 20 >= y:
            den += 1
        else:
            fora += 1
    
    print('%i in' %(den))
    print('%i out' %(fora))

main()