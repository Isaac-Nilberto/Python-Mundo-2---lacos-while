#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 22:50:14 2024

@author: isaacnilberto
"""

"""
Faca um programa que leia um numero qualquer e mostre o seu fatorial.

exemplo:

numero = float(input('Digite um numero para calcular o fatorial: '))
numero = 5 

5! = 5*4*3*2*1 = 120 
"""

num_fat = int(input('Entre com o valor que desejas fazer o fatorial: '))

if num_fat < 0:
    print('O fatorial de numeros negativos nao estao sendo valculados')
elif num_fat == 0:
    print(f'O fatorial de 0 e 1.')
else:
    contador = 1
    fatorial =1
    
    while contador <= num_fat:
        fatorial = fatorial * contador
        contador = contador + 1
    print(f'O fatorial de {num_fat} e {fatorial}.')