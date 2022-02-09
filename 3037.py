# -*- coding: utf-8 -*-


n = int( input() )
i = 0

xxj = []
ddj = []

xxm = []
ddm = []

ii = 0

gatilho = False

pontosTemp = 0
pontosj = 0
pontosm = 0


resultado = []

while (i < n):
    if (gatilho == False):
        while (ii < 3):
            x, d = input().split()
            x = int(x)
            d = int(d)
            pontosTemp = x*d
            pontosj += pontosTemp
            xxj.append(x)
            ddj.append(d)
            ii += 1
        ii = 0
        gatilho = True

    if (gatilho == True):
        while (ii < 3):
            x, d = input().split()
            x = int(x)
            d = int(d)
            pontosTemp = x*d
            pontosm += pontosTemp
            xxm.append(x)
            ddm.append(d)
            ii += 1
        ii = 0
        gatilho = False

    if (pontosj > pontosm):
        resultado.append("JOAO")
    else:
        resultado.append("MARIA")

    pontosj = 0
    pontosm = 0

    i += 1

ii = 0

for ii in resultado:
    print(ii)