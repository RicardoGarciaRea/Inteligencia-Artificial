# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 10:45:59 2020

@author: Propietario
"""

import json

def caballos():
    with open ("caballosJson.json", "r") as read_file:
        data = json.load(read_file)
        inicial = data['inicial']
        final = data['final']
        grafo = data['grafo']
        referencias=[]
        guardando=[]
        tableroNumerico=[[0,1,2],[3,4,5],[6,7,8]]
        movimientos=[]
        compara=[]
        vueltas=0
        

        for tabnum in tableroNumerico:
            for tn in tabnum:
                fila=tableroNumerico.index(tabnum)
                columna=tabnum.index(tn)
                
                inserta=[tn,fila,columna];
                referencias.append(inserta)
            

        print()
        for ini in inicial:
            print(ini)
        print("--------------------------------------------")
        iguales=True;
        while iguales:
            f=0
            c=0
            
            for ini in inicial:
                for i in ini:
                    if i==1 or i==-1:
                        g=[i,f,c]
                        guardando.append(g)
                    c=c+1;
                c=0
                f=f+1;

            c=0
            f=0
            for gua in guardando:
                inicial[gua[1]][gua[2]]=0
                for r in referencias:
                    if gua[1]==r[1] and gua[2]==r[2]:
                        for gra in grafo:
                            if r[0] == gra[0]:
                                comp=gua[0],gra[2]
                                compara.append(comp)
            moverCaballos=[]
            for com in compara:
                for tn in referencias:
                    if com[1] == tn[0]:
                        mcc=[com[0],tn[1],tn[2]]
                        moverCaballos.append(mcc)
            
            for mov in moverCaballos:
                inicial[mov[1]][mov[2]]=mov[0]
            
            
            
            for ini in inicial:
                print(ini)            
            
            if inicial == final:
                iguales = False
                print("uy kieto v:")

            vueltas=vueltas+1;

            movimientos=[]
            guardando=[]
            moverCaballos=[]
            compara=[]
            print("-------------------------------------------- Estado ",vueltas)

caballos()