# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 11:49:08 2020

@author: Propietario
"""


import json

def anchura():
    print("Recorrido por anchura<-------------------------------->")
    with open ("recorrido.json", "r") as read_file:
        data = json.load(read_file)
        nodos = data['nodos']
        
    listaBorrable=[]
    
    while nodos:
        padre=nodos[0][0]
        print(padre)
        for nodo in nodos:
            if nodo[0] == padre:
                listaBorrable.append(nodo[1])
                listaBorrable = list(set(listaBorrable))
                nodos.pop(0)
                
        print(listaBorrable)
        
        
        
        
        listaBorrable=[]
        
    
    print(listaBorrable)
    listaBorrable=[]

anchura()

#----------------------------------------------------------------------------------------------
def profundidad():
    print("Recorrido por profundidad^--------------------------v")
    with open ("recorrido.json", "r") as read_file:
        data = json.load(read_file)
        nodos = data['nodos']
    
    
    listaBorrarOriginal=[]

    while nodos:
        
        listaBorrarOriginal=[]
        pivote=nodos[0][0]
        pivote2=""
        print(pivote)
        
        for nodo in  nodos:

            if pivote == nodo[0]:
                pivote = nodo[1]
                print(pivote)
                listaBorrarOriginal.append(nodos.index(nodo))
                
            

        
        for lbo in reversed(listaBorrarOriginal): 
            nodos.pop(lbo)
            
            
        
        
        listaBorrarOriginal=[]
        
        x=(len(nodos))-1
        
        pivote=nodos[x][1]
        print(pivote)
        
        for nodo in reversed(nodos):
            if pivote == nodo[1]:
                pivote = nodo[0]
                listaBorrarOriginal.append(nodos.index(nodo))
                
        for lbo in listaBorrarOriginal:
            nodos.pop(lbo)
                

profundidad()