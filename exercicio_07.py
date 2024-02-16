#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 22:57:42 2024

@author: isaacnilberto
"""

"""
Escreva um programa que leia um numero n inteiro qualquer e mostre os n pri-
meiros elementos de uma sequencia de Finonacci.

1 -> 1 -> 2 -> 3 -> 5 -> 8
"""
n = int(input('Entre com o valor do numero inteiro que voce deseja saber a serie de Fibonacci: '))

n_anterior = 0
n_atual = 1
soma = 0

contador = 0

while contador < n:
    print(n_atual)
    n_anterior, n_atual = n_atual, n_anterior + n_atual
    contador += 1
    
    