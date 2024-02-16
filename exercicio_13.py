#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:20:57 2024

@author: isaacnilberto
"""

'''
Faca um programa que jogue par ou impar com o computador. O jogo sera interrom-
pido quando o jogador perder, mostrando o total de vitorias consecutivas que ele
conquistou no final do jogo.
'''
import random
lista_par_impar = ['PAR', 'IMPAR']
vitorias = 0

while True:
    opcao = str(input('Voce quer Par ou Impar: ')).capitalize()
    print('='*30)
    while opcao not in ['Par', 'Impar']:
        print('Voce digitou errado!')
        opcao = str(input('Voce quer Par ou Impar: ')).capitalize()
    valor = int(input('Escolha o valor: '))
    print('='*30)
    computador = random.randint(0,10)
    print(f'O computador jogou {computador}.')
    print('='*30)
    soma = valor + computador
    print('O resultado ...')
    if (soma % 2 == 0 and opcao == 'Par') or (soma % 2 != 0 and opcao == 'Impar'):
        print(f'Voce ganhou e o resultado foi {soma}.')
        print('='*30)
        vitorias += 1
    else:
        print(f'Voce perdeu! O resultado foi {soma}.')
        print('='*30)
        break

print(f'Voce teve {vitorias} vitorias.')  