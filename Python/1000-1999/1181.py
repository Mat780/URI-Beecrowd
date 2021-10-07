def main():
    l1 = [ [ 0 for y in range(12) ] for x in range(12) ]
    linha = int(input())
    op = input()
    lin = 0
    col = 0
    res = 0

    for l in range(12):
        for c in range(12):
            l1[l][c] = float(input())
    
    for c in range(12):
        res += l1[linha][c]
    
    if op == 'S':
        print("%.1f" %(res))
    else:
        res /= 12
        print("%.1f" %(res))
        

main()