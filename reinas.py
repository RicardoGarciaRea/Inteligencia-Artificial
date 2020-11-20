tablero = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
fil = 0
colu = 0

def fila(A,F,C):
    if not A:
        return
    col(A[0],F,C)
    F = F + 1
    fila(A[1:],F,C)

def col(tab,F,C):
    if not tab:
        return
    if(tab[0] == 0):
        putQueen(F,C)
    C = C + 1
    col(tab[1:],F,C)

def putQueen(f,c):
    if(tablero[f][c] == 0):
        tablero[f][c] = 1
        ocuparColumnas(0,c)
        ocuparFilas(f,0)
        ocuparDiagonalPos(f,c)
        ocuparDiagonalInv(f,c)
        ocuparDiagonalNeg(f,c)
        ocuparDiagonalInvPos(f,c)

def ocuparFilas(f,c):
    if(c < 4):
        if(tablero[f][c] != 1):
            tablero[f][c] = 2
        ocuparFilas(f,c+1)

def ocuparColumnas(f,c):
    if(f < 4):
        if(tablero[f][c] != 1):
            tablero[f][c] = 2
        ocuparColumnas(f+1,c)

def ocuparDiagonalPos(f,c):
    if(f < 3 and c < 3):
        f = f + 1
        c = c + 1
        if(tablero[f][c] != 1):
            tablero[f][c] = 2
        ocuparDiagonalPos(f,c)

def ocuparDiagonalNeg(f,c):
    if(f > 0 and c > 0):
        f = f - 1
        c = c - 1
        if(tablero[f][c] != 1):
            tablero[f][c] = 2
        ocuparDiagonalNeg(f,c)


def ocuparDiagonalInv(f,c):
    if(f < 3 and c > 0):
        f = f + 1
        c = c - 1
        if(tablero[f][c] != 1):
            tablero[f][c] = 2
        ocuparDiagonalInv(f,c)

def ocuparDiagonalInvPos(f,c):
    if(f > 0 and c < 3):
        f = f - 1
        c = c + 1
        if(tablero[f][c] != 1):
            tablero[f][c] = 2
        ocuparDiagonalInvPos(f,c)


def inicio(p1,p2):
    putQueen(p1,p2)
    fila(tablero,fil,colu)
    print(tablero)


#Aqui idicamos en que posiscion se podra la primer reina
inicio(1,1)