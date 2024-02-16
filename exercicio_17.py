#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:37:51 2024

@author: isaacnilberto
"""

'''
Crie um programa que simule o funcionamento de um caixa eletronico. No inicio,
pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e o programa
vai informar quantas cedulas de cada valor serao entregues.

obs. considere que o caixa possui cedulas de 50, 20, 10 e 1.
'''

cedula = 0
print('O caixa possui cedulas de 50, 20, 10 e 1.')

while True:
    valor = int(input('Qual valor tu desejas sacar? '))
    
    #while valor !=0:
    valor = valor / 50
    print(valor)
                  