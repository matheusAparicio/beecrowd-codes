# -*- coding: utf-8 -*-

a = []
i = 0
b = 0
c = 0

while i < 100:
    i += 1
    a.append(int(input()))
    if a[i - 1] > b: b = a[i - 1]; c = i

print(b)
print(c)