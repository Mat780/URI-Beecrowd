def main():
    i = 1
    j = 7
    while i != 9 or j != 4:
        print('I=%i J=%i' %(i, j))
        j -= 1
        if j == 4 and i != 9:
            j = 7
            i += 2
        
main()