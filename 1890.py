# -*- coding: utf-8 -*-


n = int( input() ) #Número de casos
i = 0 #Índice pro loop que pegará os valores

cc = [] #Array que armazena os valores c
dd = [] #Array que armazena os valores d
ii = 0 #Índice da array para fazer o loop do cálculo

resultadoTemp = 0 #Resultado temporário de determinado caso de teste, do qual muda constantemente
resultado = [] #Array que armazena os resultados
iii = 0 #Índice do loop que mostra os resultados

#Loop para armazenar os valores
while (i < n):
    c, d = input().split()
    c = int(c)
    d = int(d)
    cc.append(c)
    dd.append(d)
    i += 1

#Loop para realizar os cálculos
while (ii < len(cc)):
    resultadoTemp = 26**cc[ii] * 10**dd[ii]
    if cc[ii] == 0 and dd[ii] == 0: resultadoTemp = 0
    resultado.append(resultadoTemp)
    ii += 1

#Loop para mostrar os resultados
while (iii < len(resultado)):
    print(resultado[iii])
    iii += 1