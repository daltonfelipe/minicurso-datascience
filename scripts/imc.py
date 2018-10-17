#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:46:21 2018

@author: dalton
"""

altura = 1.86
massa = 73.7

imc = massa/(pow(altura, 2))

if imc < 17:
    print("Abaixo do peso!")
elif imc > 17 and imc < 25:
    print("Peso normal!")
elif imc > 25:
    print("Acima do peso!")


print("Altura: %.2f, Massa: %.2f\nO imc eh: %.2f"%(altura, massa, imc))


