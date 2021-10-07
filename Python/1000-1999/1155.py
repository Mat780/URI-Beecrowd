def main():
    s = 0
    deno = 1

    while deno <= 100:
        s += 1/deno
        deno += 1
    
    print("%.2f" %(s))
main()