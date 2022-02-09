# -*- coding: utf-8 -*-

num = int(input())
i = 0
z = 0
a = []
X = 0
Y = 0
d = 0

while i < num:
    i += 1
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    x = X
    y = Y
    d = 0
    if X > Y:
        while Y < X:
            if (Y / 2) == (Y // 2):
                Y += 1
            else:
                if (Y != y): d += Y
                Y += 2
        a.append(d)
    elif X <= Y:
        while Y > X:
            if (X / 2) == (X // 2):
                X += 1
            else:
                if (X != x): d += X
                X += 2
        a.append(d)



try:
    while z < len(a):
        z += 1
        print(a[z - 1])
except:
    print("opa")