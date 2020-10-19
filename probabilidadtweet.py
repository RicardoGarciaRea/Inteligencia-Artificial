# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 19:29:27 2020

@author: Propietario
"""

import json 
Conocimiento = False

with open ("probabilidad-conocimiento.json", "r") as read_file:
    data = json.load(read_file)
    conocimiento = data['Probabilidades']

fic = open('tweet.txt', "r")
lines = list(fic)




def p():    
    pila = []
    separaContenido = lines[0].split(" ")
    for sc in separaContenido:
        for prob in conocimiento:
            if sc == prob[0]:
                datos=prob[0],prob[1]
                pila.append(datos)
                
    print(pila)
    promedio=0
    for p in pila:
        print(p[1])
        promedio=promedio+float(p[1])
    promedio=promedio/len(pila)
    
    if promedio > .55:
        print("Stream")
    else:
        print("no es stream")

   