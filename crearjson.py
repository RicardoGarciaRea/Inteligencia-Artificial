#import json
#import os
# -*- coding: utf-8 -*-

#file = open("C:/Users/p/.spyder-py3/datos2.json", "w")
#file.write("Primera línea" + os.linesep)
#file.write("Segunda línea")
#file.close()
import json 
import sys
import os


conocimiento = False


with open ("tweets2.json", "r") as read_file:
    data = json.load(read_file)
    conocimiento = data['Tweets']
    
palabras =	["Vamos","Bloodborne","darle","seguirle","acompañenme",	"claro","continuarle","FALL"
            ,"GUYS","Martes","nueva","Raider","ratito","Sheep","sufrir","temporada",
			"terror","niño"]


def enie():
    cont=0
    for p in palabras:
        validar = str.__contains__(p, "ñ")
        if validar:
            x=p
            b=x.replace("ñ", "Ã±")
            palabras.pop(cont)
            palabras.append(b)
        cont=cont+1
    

def crear():
    
    enie()
    
    pila=[]
    numeros = []
    for p in palabras:
        contador_prob=0
        for c in conocimiento:
            validar = str.__contains__(c['texto'], p)
            if validar == True:
                ant=contador_prob
                contador_prob=contador_prob+1            
                ap=p," ",contador_prob        
        pila.append(ap)
        numeros.append(contador_prob)
        print(max(numeros))

    

    coma=0
    file = open("C:/Users/p/.spyder-py3/datos2.json", "w")
    file.write('{	\n	"Probabilidades": [ \n')
    for pi in pila:
        cast = float(pi[2])
        probabilidad = cast / max(numeros)
        if coma == len(pila)-1:
            x=str('["')+str(pi[0])+str('",')+str(probabilidad)+str("] \n")
        else:
            x=str('["')+str(pi[0])+str('",')+str(probabilidad)+str("], \n")
    #file.write('["')
        file.write(x)
        print(x)
        coma=coma+1
    file.write("] \n }")
    file.close()