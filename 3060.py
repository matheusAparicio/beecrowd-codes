# -*- coding: utf-8 -*-

#Input dos valores a e b.
v = int ( input() )
p = int ( input() )

#Resto padrão.
resto = 1

resultado = int(v / p) #Variável resultado (será equivalente ao quociente)

i = 0 #Índice do primeiro loop.
ii = 0 #Índice do segundo loop.

#Quociente começando no 0.
quociente = 0


if (v / p) == (v // p): #Caso seja uma divisão exata.
    while (i < p):
        print(resultado)
        i += 1
else: #Caso não seja uma divisão exata.
    while (p * quociente < v): #Descobrir qual o maior quociente possível.
        quociente += 1
    quociente -= 1 #Diminuir o quociente em 1 para permitir que a seja maior que p*quociente.
    resto = (v - (p * quociente))
    resultado = quociente

    #Mostrar o resultado
    while (ii < p):
        if resto > 0: #Se ainda existir resto maior que 0, adicionar às primeiras parcelas.
            resto -= 1
            print(resultado + 1)
        else: #Caso o resto seja nulo, exibir as parcelas normais.
            print(resultado)

        ii += 1 #Aumentar o índice do loop.