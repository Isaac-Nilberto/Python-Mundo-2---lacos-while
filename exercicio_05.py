#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 22:53:33 2024

@author: isaacnilberto
"""

"""
Faca um programa que leia o primeiro termo de uma P.A e a razao da P.A,
mostrando os 10 primeiros termos dela usando a estrutura while.
"""

a_1 = int(input('Entre com o primeiro termo: '))

razao = int(input('Entre com o valor da razao da P.A.: '))
contador = 0

while contador < 10:
    a_n = a_1 + (contador * razao) 
    print(f'O valor da p.a e {a_n}.')
    contador += 1
