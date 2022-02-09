# -*- coding: utf-8 -*-

num_ar = int(input())
num = num_ar
nota_cem = 0
nota_cinquenta = 0
nota_vinte = 0
nota_dez = 0
nota_cinco = 0
nota_dois = 0
nota_um = 0

while num_ar >= 100:
    nota_cem += 1
    num_ar -= 100

while num_ar >= 50:
    nota_cinquenta += 1
    num_ar -= 50

while num_ar >= 20:
    nota_vinte += 1
    num_ar -= 20

while num_ar >= 10:
    nota_dez += 1
    num_ar -= 10

while num_ar >= 5:
    nota_cinco += 1
    num_ar -= 5

while num_ar >= 2:
    nota_dois += 1
    num_ar -= 2

while num_ar >= 1.00:
    nota_um += 1
    num_ar -= 1.00

print("%d\n%d nota(s) de R$ 100,00\n%d nota(s) de R$ 50,00\n%d nota(s) de R$ 20,00\n%d nota(s) de R$ 10,00\n%s nota(s) de R$ 5,00\n%d nota(s) de R$ 2,00\n%d nota(s) de R$ 1,00"
%(num, nota_cem, nota_cinquenta, nota_vinte, nota_dez, nota_cinco, nota_dois, nota_um)
)