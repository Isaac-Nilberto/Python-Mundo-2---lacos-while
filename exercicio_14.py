#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:21:08 2024

@author: isaacnilberto
"""

'''
Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuario quer ou nao continuar.
No final mostre:
    
    a) quantas pessoas tem mais de 18 anos
    b) quantos homens foram cadastrados
    c) quantas mulheres tem menos de 20 anos
'''
contador = 0
maior_dezoito = 0
homens = 0
mulheres = 0
while True:
    contador += 1
    idade = int(input('Entre com a sua idade: '))
    sexo = str(input('Qual seu sexo?[F/M] '))
    
    if idade > 18:
        maior_dezoito += 1
    
    if sexo in 'Mm':
        homens += 1
    
    if sexo in 'Ff':
        if idade < 20:
            mulheres += 1
    while sexo not in 'FfMm':
        print('Voce digitou errado: ')
        sexo = str(input('Qual seu sexo? '))
    
    continuador = str(input('Voce quer continuar: [S/N]'))
    while continuador not in 'SsNn':
        print('Voce digitou errado: ')
        continuador = str(input('Voce quer continuar? '))
    if continuador in 'Nn':
        print('Quiseste terminar, égua!')
        break
    
print(f'Foram cadastradas ', contador,'pessoas.')
print(f'O numero de pessoas maiores de 18 cadastradas foram ', maior_dezoito,'pessoa(s).')
print(f'O numero de mulheres menores que 20 anos cadastradas foram ', mulheres,'pessoa(s).')
print(f'O numero de pessoas homens cadastrados foram ', homens,'pessoa(s).')
