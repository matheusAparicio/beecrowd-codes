# -*- coding: utf-8 -*-

n = int( input() ) #Número de testes.
i = 0 #Índice do loop.

carater = 0 #Se é verba ou gasto para a UFSC.
valor = 0 #O valor da verba/gasto.

saldo = 0 #O saldo final da UFSC.

#Loop
while (i < n):
    carater, valor = input().split()
    carater = str(carater)
    valor = int(valor)
    if (carater == "V"): #Se for verba adicionar o valor ao saldo.
        saldo += valor
    elif (carater == "G"): #Se for gasto subtrair o valor ao saldo.
        saldo -= valor
    i += 1

#Resultado
if (saldo < 0):
    print("NAO VAI TER CORTE, VAI TER LUTA!")
else:
    print("A greve vai parar.")