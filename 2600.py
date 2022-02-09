# -*- coding: utf-8 -*-

num = int(input())
resultado = []

while num > 0:

    d1 = int(input())
    d2, d3, d4, d5 = input().split()
    d6 = int(input())
    d2 = int(d2)
    d3 = int(d3)
    d4 = int(d4)
    d5 = int(d5)

    if (d1 + d6 == 7) and (d2 + d4 == 7) and (d3 + d5 == 7) and (d1 * d2 * d3 * d4 * d5 * d6) == 720:
        resultado.append("SIM")
    else:
        resultado.append("NAO")

    num -= 1

for x in resultado:
    print(x)