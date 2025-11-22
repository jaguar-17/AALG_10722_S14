def impMat(mat):
    for fil in mat:
        print(fil)
    print()

def caminosFB(lab, f, c):
    global op
    op += 1
    if f == len(lab)-1 and c == len(lab[0])-1:
        if lab[f][c] == 1:
            return 1
        else:
            return 0
    elif c == len(lab[0])-1:
        if lab[f][c] == 1:
            return caminosFB(lab, f+1, c)
        else:
            return 0
    elif f == len(lab)-1:
        if lab[f][c] == 1:
            return caminosFB(lab, f, c+1)
        else:
            return 0
    else:
        if lab[f][c] == 1:
            return caminosFB(lab, f, c+1) + caminosFB(lab, f+1, c)
        else:
            return 0

def caminosPD(tabla, lab, f, c):
    global op
    op += 1
    #print(f"f{f} c{c}")
    #impMat(tabla)
    if tabla[f][c] != -1:
        return tabla[f][c]
    elif f == len(lab)-1 and c == len(lab[0])-1:
        if lab[f][c] == 1:
            tabla[f][c] = 1
            return tabla[f][c]
        else:
            tabla[f][c] = 0
            return 0
    elif c == len(lab[0])-1:
        if lab[f][c] == 1:
            tabla[f][c] = caminosPD(tabla, lab, f+1, c)
            return tabla[f][c]
        else:
            tabla[f][c] = 0
            return 0
    elif f == len(lab)-1:
        if lab[f][c] == 1:
            tabla[f][c] = caminosPD(tabla, lab, f, c+1)
            return tabla[f][c]
        else:
            tabla[f][c] = 0
            return 0
    else:
        if lab[f][c] == 1:
            tabla[f][c] = caminosPD(tabla, lab, f, c+1) + caminosPD(tabla, lab, f+1, c)
            return tabla[f][c]
        else:
            tabla[f][c] = 0
            return 0


    
lab = [
    [1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,0,1],
    [1,1,1,1,0,1,1,1],
    [0,1,0,1,1,0,1,1],
    [1,1,0,1,1,1,1,1],
    [1,1,1,0,0,1,0,1],
    [1,0,1,1,1,0,1,1],
    [1,1,1,1,1,1,1,1]
]

tabla = [[-1 for _ in range(len(lab)) ] for x in range(len(lab)) ]

op = 0
res = caminosPD(tabla, lab, 0, 0)
print(f"En PD hay {res} caminos (ops:{op})")
#impMat(tabla)
op = 0
res = caminosFB(lab, 0, 0)
print(f"En FB hay {res} caminos (ops:{op})")
