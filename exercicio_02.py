#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 22:43:54 2024

@author: isaacnilberto
"""

"""
Faca um programa onde o computador vai pensar num numero entre
0 e 10. Onde o jogador vai tentar ate advinhar, mostrando no final
quantos palpites foram necessarios para vencer
"""
import random


numero_computador = random.randint(1,10)
numero_jogador = int(input('Entre com um numero inteiro: '))
tentativa = 1
while numero_jogador != numero_computador:
    tentativa += 1
    numero_jogador = int(input('Numero errado. Entre com o numero correto: '))
print(f'O numero de tentativas foi {tentativa}')
print(f'O numero escolhido pela maquina foi {numero_computador}.')