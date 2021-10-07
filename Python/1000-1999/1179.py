def main():
    par = []
    impar = []

    for c in range(15):
        num = int(input())
        if num%2 == 0:
            par.append(num)
        else:
            impar.append(num)
        
        if len(par) == 5:
            for i in range(5):
                print("par[%i] = %i" %(i, par[i]))
            par = []
        elif len(impar) == 5:
            for i in range(5):
                print("impar[%i] = %i" %(i, impar[i]))
            impar = []

    for i in range(len(impar)):
                print("impar[%i] = %i" %(i, impar[i]))
    for i in range(len(par)):
                print("par[%i] = %i" %(i, par[i]))

main()