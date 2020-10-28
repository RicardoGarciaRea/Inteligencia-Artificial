# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:22:03 2020

@author: Propietario
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:22:03 2020

@author: Propietario
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 19:34:39 2020

@author: Propietario
"""

import json

evitar = ['¿', '?', '¡', '!', '-', '+', ',', ':', ';', '@', '#', 'a', 'con', 'de', 'en', 'hacia', 'para', 'por', 'sin', 'hasta', 'contra', 'segun',
               'sobre', 'tras', 'ante', 'bajo','sã­',
               'desde', 'antes', 'respecto', 'lejos', 'el', 'la', 'lo', 'los', 'las', 'ahi', 'allí', 'aquí', 'acá', 'delante', 'detrás', 'arriba', 'abajo', 'cerca', 'lejos', 'encima',
          'fuera', 'dentro', 'ya', 'aún', 'tarde', 'pronto', 'todavía', 'ayer',
          'recién', 'nunca', 'siempre', 'jamás', 'ahora', 'mal', 'bien', 'regular',
          'despacio', 'así', 'mejor', 'peor', 'similar', 'fácilmente', 'muy', 'más', 'me', 'cuando', 'ni', 'esta', 'y',
          'poco', 'bastabte', 'demasiado', 'menos', 'mucho', 'algo', 'casi', 'tal vez', 'le', 'mis',
          'acaso', 'quizás', 'que', 'este', 'sí', 'un', 'al', '0', '1', '2', '3', '5', '6', '7', '8', '9']

segundofiltro = [':', '(', ')', '=', '¿', '?', '¡', '!',
                 '-', '+', ',', ':', ';', '@', '#', '.','0','1','2','3','4','5','6','7','8','9']

def abrir():
    with open("tweets2.json", "r") as read_file:
        data = json.load(read_file)
        conocimiento = data['Tweets']
    print (conocimiento)

    tweetConca = []
    for c in conocimiento:
        if c['Stream']:
            palabraTexto = c['texto'].split(" ")
            for pa in palabraTexto:
                pa = pa.lower()
                tweetConca.append(pa)

    #print(tweetConca)
    tuit = ""
    for t in tweetConca:
        tuit = tuit+str(" ")+str(t)


    tweet = tuit

    for t in tweet:
        for sf in segundofiltro:
            tweet = tweet.replace(sf, "")

    tweet = tweet.lower()
    letters = tweet.split(" ")


    def filterVowels(letter):
        
        if(letter not in evitar):
            return True
        else:
            return False


    tweetFiltrado = filter(filterVowels, letters)
    #print(tweetFiltrado)


    pilaResultado = []
    #print('tweet filtrado')
    #print('')

    for palabra in tweetFiltrado:
        #print(palabra, "-----")
        for sf in segundofiltro:
            if str.__contains__(palabra, sf):
                palabra = palabra.replace(sf, "")
            if palabra != "":
                pilaResultado.append(palabra)

    #print(pilaResultado)
    generarjson(pilaResultado)




def generarjson(pilaResultado):
    
    #print("--------------------")
    lista2 = []
    maximo = 0
    for w in pilaResultado:
        for l in lista2:
            if maximo < l[1]:
                maximo = l[1]
        x = w, pilaResultado.count(w)
        lista2.append(x)


    mj2 = sorted(set(lista2))
    #print(maximo)

    coma = 0
    file = open("C:/Users/p/.spyder-py3/datos2.json", "w")
    file.write('{	\n	"Probabilidades": [ \n')
    for pi in mj2:
        cast = float(pi[1])
        probabilidad = cast / maximo
        if coma == len(mj2)-1:
            x = str('["')+str(pi[0])+str('",')+str(probabilidad)+str("] \n")
        else:
            x = str('["')+str(pi[0])+str('",')+str(probabilidad)+str("], \n")
        file.write(x)
        #print(x)
        coma = coma+1
    file.write("] \n }")
    file.close()
