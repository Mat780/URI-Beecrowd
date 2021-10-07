def main():
    l1 = list(map(int, input().split()))
    i = 1
    res = 0

    while l1[i] <= 0:
        if l1[i] <=0:
            i += 1
        if l1[i] > 0:
            break

    for c in range(0,l1[i]):
        res += l1[0] + c
    print(res)
main()