#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 17:15:38 2018

@author: dalton
"""

notas = []

for i in range(3):
    notas.append(int(input("Digite nota %d: "%(i+1))))

media = sum(notas)/3

if media>=6 and media<10:
    print("Media: {}\tStatus: {}".format(media, "aprovado"))
elif media == 10.0:
    print("Media: {}\tStatus: {}".format(media, "excelente"))
else:
    print("Media: {}\tStatus: {}".format(media, "substitutiva"))
    