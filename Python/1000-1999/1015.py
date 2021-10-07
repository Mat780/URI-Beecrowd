# -*- coding: utf-8 -*-

def main():
    l1 = input().split(" ")
    l2 = input().split(" ")
    x1 = float(l1[0])
    y1 = float(l1[1])
    x2 = float(l2[0])
    y2 = float(l2[1])
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    print("%.4f" %d)
main()