#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 23:04:31 2024

@author: isaacnilberto
"""

"""
Crie um programa que leia varios numeros inteiros pelo teclado. No final da
execucao, mostre a media entre todos os valores e qual foi o maior e o menor
valores lidos. O programa deve perguntar se ele quer ou nao continuar a
digitar valores.
"""

soma = 0
repeticoes = 0
num_min = float('inf')
num_max = float('-inf')

while True:
    repeticoes += 1
    valor = int(input('Entre com um valor: '))
    soma = soma + valor
    resposta = str(input('Desejas continuar? [S] ou [N]: '))
    
    if valor < num_min:
        num_min = valor
    if valor > num_max:
        num_max = valor
    
    if resposta in 'Nn':
        print('Voce quis encerrar o programa. Espero-te logo mais.')
        break
    if resposta in 'Ss':
        print('Vamos continuar! Que beleza.')
    while resposta not in 'SsNn':
        print('Voce digitou errado! Tente novamente!')
        resposta = str(input('Desejas continuar? [S] ou [N]: '))
media = soma / repeticoes
print('='*30)
print(f'O valor da media é {media}.')
print('='*30)
print(f'O menor valor é {num_min} e o maior valor é {num_max}.')
#%%%%%
