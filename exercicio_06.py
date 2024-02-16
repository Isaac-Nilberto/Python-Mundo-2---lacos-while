#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 22:56:13 2024

@author: isaacnilberto
"""

"""
Melhore o exercicio anterior perguntando para o usuario se ele quer mostrar
mais alguns termos. O programa encerra quando ele disser que quer mostrar 0
termos.
"""

a_1 = int(input('Entre com o valor do primeiro termo: '))
razao = int(input('Entre com o valor da razao: '))
contador = 0
continuador = 10
total = 0

while continuador != 0:
    total = total + continuador
    while contador < total:
        a_n = a_1 + (contador * razao)
        print(a_n)
        contador += 1
    continuador = int(input('Quantos temos a mais desejas ver? '))