# -*- coding: utf-8 -*-

a, b, c = input().split()
x, y, z = input().split()

a = int(a); b = int(b); c = int(c); x = int(x); y = int(y); z = int(z)

print( (x // a) * (y // b) * (z // c) )