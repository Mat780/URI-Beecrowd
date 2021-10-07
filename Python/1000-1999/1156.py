def main():
    s = 0
    deno = 1
    num = 1

    while num <= 39:
        s += num/deno
        deno += deno
        num += 2
    
    print("%.2f" %(s))
main()