# -*- coding: utf-8 -*-

#Número de runas e nível de amizade necessário para vencer.
n, g = input().split()

n = int(n)
g = int(g)

#Nível de amizade.
amizade = 0

#Índices dos loops.
i = 0
ii = 0

#Listas para armazenar a letra correspondente a runa e seu valor de amizade.
runas = []
valores = []

#Loop para receber as letras e valores das runas.
while i < n:
    x, y = input().split()
    y = int(y)

    runas.append(x)
    valores.append(y)

    i += 1

#Número de runas recitadas por Sam e Frodo, assim como suas letras correspondentes.
a = int( input() )
nn = list(map(str, input().split()))

#Loop para descobrir o valor da amizade depois do recitamento das runas.
for runaAtual in nn:
    while ii < n:
        if runas[ii] == runaAtual:
            amizade += valores[ii]
        ii += 1
    ii = 0

#Printar o nível de amizade.
print(amizade)

#Printar se Sam e Frodo ganharam ou não.
if amizade >= g:
    print("You shall pass!")
else:
    print("My precioooous")