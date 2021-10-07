from math import sqrt

while True:
    try:
        entrada = input()
        R1, X1, Y1, R2, X2, Y2 = map(int, entrada.split(' '))
        d = sqrt((X1 - X2)**2 + (Y1 - Y2)**2)
        print("RICO" if R1 >= R2+d else "MORTO")
    except EOFError:
        break