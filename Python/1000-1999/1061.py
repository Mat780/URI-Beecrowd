def main():
    l1 = input().split(' ')
    d1 = int(l1[1])

    l1 = input().split(' : ')
    h1 = int(l1[0])
    m1 = int(l1[1])
    s1 = int(l1[2])

    l1 = input().split(' ')
    d2 = int(l1[1])

    l1 = input().split(' : ')
    h2 = int(l1[0])
    m2 = int(l1[1])
    s2 = int(l1[2])

    mSeg = 60
    hSeg = mSeg * 60
    dSeg = hSeg * 24

    dS = d1 * dSeg + h1 * hSeg + m1 * mSeg + s1
    dF = d2 * dSeg + h2 * hSeg + m2 * mSeg + s2
    if dF > dS:
        temp = dF - dS
        df = int(temp / dSeg)
        temp %= dSeg  
        hf = int(temp / hSeg)
        temp %= hSeg
        mf = int(temp / mSeg)
        temp %= mSeg
        sf = int(temp)

        print('%i dia(s)' %(df))
        print('%i hora(s)' %(hf))
        print('%i minuto(s)' %(mf))
        print('%i segundo(s)' %(sf))
main()