def main():
    while True:
        x, y = map(int, input().split())

        if x == 0:
            break
        elif x > 0:
            x = 'X+'
        elif x < 0:
            x = 'X-'
        if y == 0:
            break
        elif y > 0:
            y = 'Y+'
        elif y < 0:
            y = 'Y-'
        
        if x == 'X+' and y == 'Y+':
            print('primeiro')
        
        elif x == 'X+' and y == 'Y-':
            print('quarto')

        elif x == 'X-' and y == 'Y+':
            print('segundo')

        elif x == 'X-' and y == 'Y-':
            print('terceiro')
main()