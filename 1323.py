# -*- coding: utf-8 -*-

num = int(input())
i = 0
x = 0
xx = 0
a = []
a.append(num)

while (num != 0):
    num = int(input())
    a.append(num)

while (i < len(a)):
    i += 1
    xx = a[i - 1]
    x = ( 2*(xx**3) + 3*(xx**2) + xx ) / 6
    if (x != 0): print(int(x))