# -*- coding: utf-8 -*-

#Número de registros.
n = int (input())

#Índices dos loops.
i = 0
ii = 0

#Lista para armazenar os registros.
registros = []

#Loop para obter o input registro e armazená-lo na lista "registros" caso ele não conste nela.
while i < n:
    registros.append( input() )
    i += 1

#Transformar os elementos da lista em chaves, impossibilitando a existência de duplicatas.
registros = list(dict.fromkeys(registros))

#Print do resultado.
print(len(registros))