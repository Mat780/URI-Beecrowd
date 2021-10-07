# -*- coding: utf-8 -*-

def main():
    v = int(input())

    for c in range(0, v):
        l = input().split()
        l1 = []
        l2 = []
        l3 = []

        for c in (l[0]):
            l1.append(c)
        for c in (l[1]):
            l2.append(c)
        
        lnt = len(l1) + len(l2)
        c = 0
        
        while True:
            if (len(l1)-1) >= c:
                l3.append(l1[c])

            if (len(l2)-1) >= c:
                l3.append(l2[c])
            
            if len(l3) == lnt:
                break

            c += 1
        
        for c in range(0, len(l3)-1):
            print(l3[c], end='')
        
        print(l3[-1])


main()