#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:20:40 2024

@author: isaacnilberto
"""

'''
Faca um programa que mostre a tabuada de varios numeros, um de cada vez, para
cada valor digitado pelo usuario. O programa sera interrompido quando o numero
solicitado for negativo.
'''
while True:
    print('Para interromper digite um numero negativo')
    print('='*30)
    valor = int(input('Digite um numero para voce saber a tabuada: '))
    if valor < 0:
        print('Terminaste o estudo? Espero-te na proxima!')
        break
    for i in range(1,11):
        print(f'A multiplicacao entre {valor} x {i} = {valor * i}')
    print('='*30)