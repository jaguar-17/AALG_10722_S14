def fiboFBR(n):
    global op
    op += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiboFBR(n - 1) + fiboFBR(n - 2)

def fiboPDTDR(n, arreglo):
    global op
    op += 1
    if arreglo[n] != -1:
        return arreglo[n]
    elif n == 0:
        arreglo[n] = 0
        return arreglo[n]
    elif n == 1:
        arreglo[n] = 1
        return arreglo[n]
    else:
        arreglo[n] = fiboPDTDR(n - 1, arreglo) + fiboPDTDR(n - 2, arreglo)
        return arreglo[n]

n = 40  

arreglo = [-1] * (n + 1)
op=0
res = fiboPDTDR(n, arreglo)
print(f"programación dinámica:{res}, (ops:{op})")
op=0
res = fiboFBR(n)
print(f"fuerza bruta:{res}, (ops:{op})")
