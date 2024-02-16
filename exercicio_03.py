#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 22:47:24 2024

@author: isaacnilberto
"""

"""
Crie um programa que leia dois valores e mostre um menu na tela

[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa

Seu programa devera realizar a operacao solicitada em cada caso.
"""

num_1 = float(input('Entre com o primeiro valor: '))

num_2 = float(input('Entre com o segundo valor: '))

print('O que voce deseja:')
print('[1] somar')
print('[2] multiplicar')
print('[3] maior ')
print('[4] novos numeros')
print('[5] sair do programa')


while True:
    num_escolhido = int(input('O que desejas fazer? '))
    print(f'Voce escolheu a opcao {num_escolhido}')
    print('#'*10)
    if num_escolhido == 1:
        soma = num_1 + num_2
        print(f'O resultado da soma e: {soma}.')
        print('#'*10)
    elif num_escolhido == 2:
        multiplicacao = num_1 * num_2
        print(f'O resultado da multiplicacao e: {multiplicacao}.')
        print('#'*10)
    elif num_escolhido == 3:
        if num_1 > num_2:
            print(f'O numero 1- {num_1}- e maior que o numero 2 -{num_2}.')
            print('#'*10)
        elif num_1 == num_2:
            print(f'O numero 1-{num_1}- e igual ao numero 2-{num_2}.')
            print('#'*10)
        else:
            print(f'O numero 1 -{num_1}- e menor que o numero 2 {num_2}.')
            print(f'')
    elif num_escolhido == 4:
        print('Voce deseja escolher novos numeros')
        num_1 = float(input('Entre com o primeiro novo valor: '))

        num_2 = float(input('Entre com o segundo novo valor: '))
    elif num_escolhido == 5:
        print('Voce desejou sair, ne? Poxa.')
        break
    else:
        print('Operacao invalida.')
        
print('Ate logo')

