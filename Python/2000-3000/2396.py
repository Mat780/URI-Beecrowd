def main():

    car , volt = map(int, input().split())

    fcars = 0
    lug1 = 999999999999999999999999999999999
    lug2 = 999999999999999999999999999999999
    lug3 = 999999999999999999999999999999999
    lvf = []

    if car >= 3:

        while car != fcars:
            volta = 0
            fcars += 1

            lv = []
            lv = input().split()

            for c in range(1, volt+1):
                temp = int(lv[c-1])
                volta += temp

            if volta < lug1:
                lug3 = lug2
                lug2 = lug1
                lug1 = volta
            
            elif volta < lug2:
                lug3 = lug2
                lug2 = volta
            
            elif volta < lug3:
                lug3 = volta

            lvf.append(volta)
            
        print(lvf.index(lug1)+1)
        print(lvf.index(lug2)+1)
        print(lvf.index(lug3)+1)
            


main()