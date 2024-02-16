#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 23:00:37 2024

@author: isaacnilberto
"""

"""
Crie um programa que leia varios inteiros pelo teclado. O programa so vai
parar quando o usuario digitar o valor 999, que e a codicao de parada. No
final mostre quantos numeros foram digitados e qual foi a soma entre eles
desconsiderando o final.
"""
soma = 0
contador = 0
while True:
    valor = int(input('Entre com um valor de um numero inteiro: '))
    print('Para você parar digite 999')
    
    if valor == 999:
        print('Por que você parou? Poxa. Espero-te na próxima.')
        break
    soma = soma + valor
    contador += 1
print(f'Voce digitou {contador} vez(es) e a soma dos numeros digitados foi: {soma}.')
    