#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:21:29 2024

@author: isaacnilberto
"""
'''
Crie um programa que leia o nome e o preco de varios produtos. O programa devera
perguntar se o usuario vai continuar. No final, mostre:
    a) qual o preco da compra
    b) quantos custam mais de 1000 reais
    c) Qual o nome do produto mais barato.
'''

soma_preco = 0
mais_mil = 0
continuador = 0
contador = 0
mais_barato = float('inf')
produto_mais_barato = ''
while True:
    contador += 1
    produto = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o valor do produto? '))
    soma_preco += preco
    continuador = str(input('Tem mais produtos?[S/N] '))
    
    if preco > 1000:
        mais_mil += 1
    
    if mais_barato > preco:
        mais_barato = preco
        produto_mais_barato = produto
    
    
    while continuador not in 'SsNn':
        print('Voce digitou errado!')
        continuador = str(input('S ou N '))
    if continuador in 'Nn':
        print('Quiseste terminar, égua!')
        break
        
print(f'Foram {contador} produtos.')
print(f'O preco pago nas compras foi de: {soma_preco}.')
print(f'Produtos maiores que mil reais: {mais_mil}.')
print(f'{produto_mais_barato} é produto mais barato custando {mais_barato} reais.')if continuador in 'Nn':
        print('Quiseste terminar, égua!')
        break