#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:18:18 2024

@author: isaacnilberto
"""

'''
Crie um programa que leia varios numeros inteiros pelo teclado. O programa so
vai parar quando o usuario digitar o valor 999, que é a condicao final.
No final, mostre quantos numeros foram digitados e qual foi a soma entre eles.
'''
soma = 0
contador = 0
while True:
    valor = int(input('Digite um numero inteiro para o nosso estudo: '))
    
    if valor == 999:
        print('Poxa, espero-te logo mais!')
        break
    
    print('-'*30)
    soma += valor
    contador += 1
    print('Para parar digite 999')
    
print('-'*30)
print(f'Voce digitou {contador} vez(es) e o valor da soma dos numeros digitados é {soma}.')