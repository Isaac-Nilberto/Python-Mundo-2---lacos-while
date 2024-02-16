#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 22:41:31 2024

@author: isaacnilberto
"""

"""
faca um programa que leia o sexo de uma pessoa, mas so aceite os valores
'mM' ou 'Fm'. Caso esteja errado, peca a digitacao novamente ate ter um valor
correto
"""
genero = str(input('Entre com o genero da pessoa [F/M]: ')).strip().upper()

while genero not in 'MmFf':
    genero = str(input('Digite novamente o genero [F/M]: ')).strip().upper()
print(f'O seu genero é: {genero}')