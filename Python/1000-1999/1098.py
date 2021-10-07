def main():
    i = 0
    j = 1
    acre = (0.2)
    while True:
        for c in range(0, 3):
            if i > 1.9:
                print('I=%i J=%i' %(2, j))

            elif i == 0 or i == 1:
                print('I=%i J=%i' %(i, j))

            else:
                print('I=%.1f J=%.1f' %(i, j))
            j += 1

        i += acre
        j = 1 + i
        if i > 2.1:
            break
main()

