from math import floor

def main():
    vez = int(input())

    for c in range(vez):
        l1 = input().split()
        pa = int(l1[0])
        pb = int(l1[1])
        g1 = float(l1[2])
        g2 = float(l1[3])
        cont = 0

        while pa <= pb:
            pa = floor(pa*(g1/100+1))
            pb = floor(pb*(g2/100+1))
            cont += 1
            if cont > 100:
                print("Mais de 1 seculo.")
                break
        if cont <= 100:
            print("%i anos." %(cont))

main()