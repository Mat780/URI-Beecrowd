# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
def main():
    l1 = input().split(" ")
    a = int(l1[0])
    b = int(l1[1])
    c = int(l1[2])

    if a > b and a > c:
        x = a
        if b > c:
            y = b
            z = c
        else:
            y = c
            z = b
    if b > a and b > c:
        x = b
        if a > c:
            y = a
            z = c
        else:
            y = c
            z = a
    if c > a and c > b:
        x = c
        if a > b:
            y = a
            z = b
        else:
            y = b
            z = a
    print("%d\n%d\n%d\n\n%d\n%d\n%d\n" %(z, y, x, a, b, c))

main()