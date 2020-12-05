import json
import random
############### Inicio mandar datos #########################
if __name__ == "__main__":
    ruta1 = './boome2/tablero.json'
    ruta2 = './boome2/data.json'

def sendData(donde, datos):
    with open("data.json") as json_file:
        data = json.load(json_file)
        data[str(donde)].update(datos)
    write_new_data(data)


def write_new_data(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def cargar_datos(ruta):
    with open(ruta) as contenido:
        tablero = json.load(contenido)
    return tablero['tablero']


def cargar_datos_fromData(ruta):
    with open(ruta) as contenido:
        tablero = json.load(contenido)
    return tablero

t = cargar_datos(ruta1)
data = cargar_datos_fromData(ruta2)
robot = []
bomba = []
estuve = []
ban = []
co = []
l = []
cont = 0

# Ejemplo de como mandar datos
#da= {"00":{"01":{"costo":1,"TotheBomb":17,"sum":18}}}
# sendDataTores(da)
####################################################################

##### Cargar Datos -> encontrar la bomba, robot, obstaculos ##################

def cordBloqueados(fila, list):
    if not list:
        return []
    if 2 in list:
        x = [fila, list.index(2)]
        ban.append(x)
        list[list.index(2)] = 0
        cordBloqueados(fila, list)

for x in t:
    if not robot:
        if(1 in x):
            robot = [cont, x.index(1)]
    if not bomba:
        if(3 in x):
            bomba = [cont, x.index(3)]
    if(2 in x):
        cordBloqueados(cont, x)
    cont += 1

#################################################

########## Se uso para definir adyacencias y calcular el valor de su distancia a la bomba #############
##Esto era para llenar data.json
'''

def fila(ex):
    if ex < 10:
        y(ex, 0)
        fila(ex+1)


def y(ex, ey):
    if ey < 10:
        cordenadas = [ex, ey]
        if cordenadas not in ban:
            adyacencias(cordenadas)
        y(ex, ey+1)


def adyacencias(list):
    x = list[0]
    y = list[1]

    xmas = x + 1
    xmen = x - 1
    ymas = y + 1
    ymen = y - 1

    ad = []
    s = []

    if(ymen > -1):
        s = [x, ymen]
        if s not in ban:
            ad.append(s)
    if(ymas < 10):
        s = [x, ymas]
        if s not in ban:
            ad.append(s)

    if xmas < 10:
        s = [xmas, y]
        if s not in ban:
            ad.append(s)
        if ymas < 10:
            s = [xmas, ymas]
            if s not in ban:
                ad.append(s)
        if ymen > -1:
            s = [xmas, ymen]
            if s not in ban:
                ad.append(s)

    if xmen > -1:
        s = [xmen, y]
        if s not in ban:
            ad.append(s)
        if ymas < 10:
            s = [xmen, ymas]
            if s not in ban:
                ad.append(s)
        if ymen > -1:
            s = [xmen, ymen]
            if s not in ban:
                ad.append(s)
    #dtb = contDist(x,y)
    # print(ad)
    #example = {"disBom":dtb,"adyacencias":ad}
    # sendData(str(x)+str(y),example)


def contDist(x, y):
    bx = bomba[0]
    by = bomba[1]
    abx = abs(bx-x)
    aby = abs(by-y)
    return (abx+aby)

'''
#############################################################################################################


def costoMov(estoy):
    cadena = str(estoy[0])+str(estoy[1])
    ad = data[cadena]['adyacencias']
    costos = []
    for new in ad:
        if new not in estuve:
            cadenaNew = str(new[0])+str(new[1])
            disB = data[cadenaNew]['disBom']
            c = cost(estoy, new)
            s = disB+c
            t[new[0]][new[1]] = s
            if new not in l:
                l.append(new)
                co.append(s)
            else:
                co[l.index(new)] = s
            costos.append(s)

def cost(r, d):
    xd = d[0]
    yd = d[1]
    xr = r[0]
    yr = r[1]
    if(((xr - 1) == xd) or ((xr + 1) == xd)):
        if(yd == yr):
            return 1
    if(((yr - 1) == yd) or ((yr + 1) == yd)):
        if(xd == xr):
            return 1
    return 2

def inicio(r):
    estuve.append(r)
    if r != bomba:
        costoMov(r)
        xs = random.choice(detMen(co))
        nr = l[xs]
        ##print("Costos", co)
        ##print("Lugares", l)
        ##print("Elegido", l[xs])
        ##print("Costos", co[xs])
        l.pop(xs)
        co.pop(xs)
        inicio(nr)

def detMen(c):
    men = min(c)
    repe = c.count(men)
    if repe == 1:
        return [c.index(men)]
    menores = []
    for i, val in enumerate(c):
        if val == men:
            menores.append(i)
    return menores

inicio(robot)

def maxVal(list,spath):
    di = []
    for x in list:
        s = str(x[0])+str(x[1])
        di.append(data[s]['disBom'])
    if len(di) > 0:
        return (list[di.index(max(di))])
    return 

def discardValues(valores,fullPath,mainPath):
    nv = []
    for x in valores:
        if x in fullPath:
            if x not in mainPath:
                nv.append(x)
    return nv

spath = []

def newPath(inicio):
    if inicio not in spath:
        spath.append(inicio)
    key = str(inicio[0])+str(inicio[1])
    pathAd = data[key]['adyacencias']
    newAd = discardValues(pathAd,estuve,spath)
    if len(newAd) == 1:
        spath.append(newAd[0])
        newPath(newAd[0])
    else:
        valores = maxVal(newAd,spath)
        if valores not in spath:
            if valores:
                spath.append(valores)
                newPath(valores)
            
newPath(bomba)
print("Pase por: ",estuve)
print("Mejor Camino:",spath)

def defPath(list):    
    for x,f in enumerate(list):
        for y,c in enumerate(f):
            cor = [x,y]
            if cor in spath:
                list[x][y] = "R"
            else:
                if cor in ban:
                    list[x][y] = 2
                else:
                    list[x][y] = 0
    return list
newt = defPath(t)
for x in newt:
    print(x)
