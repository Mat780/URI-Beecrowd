# -*- coding: utf-8 -*-

def main():
    s = int(input())
    h = s//60**2
    s = s - h * 60**2
    m = s//60
    s = s - m * 60
    print("{}:{}:{}".format(h,m,s))
main()