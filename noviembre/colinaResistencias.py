# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:57:34 2020

@author: Propietario
"""

import json
import random
def colina():
    print("Recorrido por mayor resistencia - ")
    with open ("datosColina.json", "r") as read_file:
        data = json.load(read_file)
        colina = data['colina']
        cont=0
        encontrado=True 
        recorrere=0
        origen="h"
        destino="l"
        numero=0
        while encontrado:

            print(origen)
            distancias=[]

            for c in colina:
                if origen == c[0]:
                    x = c[1], c[2]
                    distancias.append(x)
            
            print(distancias)
                
            comparar=distancias[0][1]
            diferentes=False
            for d in distancias:
                if comparar != d[1]:
                    diferentes=True

            listanumero=[]
            
            for d in distancias:
                listanumero.append(d[1])
                
            if cont < 20:
                ma = max(listanumero)
                print("ejecutando resistencia mayor +++++++++++++++")
            else:
                ma = min(listanumero)
                print("ejecutando resistencia menor ---------------")
            
            indice = listanumero.index(ma)
            print(indice," este es el indice")
            ira=distancias[indice]
            print(ira," este es el lugar a donde ira")
    
            print(ira)
            if diferentes == True:

                movermehacia=ira[0]
                recorrere=recorrere+ira[1]
                origen=movermehacia
                print(origen)
            if diferentes == False:

                numero = random.randint(0, len(distancias)-1)
                movermehacia=distancias[numero][0]
                recorrere=recorrere+ira[1]
                origen=movermehacia
                
                print(origen)
            cont=cont+1
            
            if origen==destino:
                encontrado=False
            
colina()