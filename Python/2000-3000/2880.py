def main():
    nigm = input()
    pal = input()
    maxiPal = len(pal)
    maxiNigm = len(nigm)+1
    contMax = 0
    auxCont = True

    for i in range(maxiNigm-maxiPal):
        aux = nigm[i:maxiPal+i]
        for c in range(maxiPal):
            if pal[c] == aux[c]:
                auxCont = False
                break
        if auxCont:
            contMax += 1
        auxCont = True
    print(contMax)    
    
main()