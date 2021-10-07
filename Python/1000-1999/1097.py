# -*- coding: utf-8 -*-

def main():
    i = 1
    j = 7
    t = 4
    while i != 9 or j != 12:
        print('I=%i J=%i' %(i, j))
        j -= 1
        if j == t and i != 9:
            j += 5
            i += 2
            t += 2
        
main()