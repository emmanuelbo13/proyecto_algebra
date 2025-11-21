# methods.py
import string

MOD = 27

#  Determinante 3x3
def determinante_3x3(M):
    a,b,c = M[0]
    d,e,f = M[1]
    g,h,i = M[2]
    return (a*e*i + b*f*g + c*d*h) - (c*e*g + b*d*i + a*f*h)

#  Inverso multiplicativo mod 27
def inverso_modular(a, mod=MOD):
    a = a % mod
    for x in range(mod):
        if (a*x) % mod == 1:
            return x
    return None  # No tiene inverso


#  Adjunta (matriz de cofactores transpuesta)
def adjunta_3x3(M):
    a,b,c = M[0]
    d,e,f = M[1]
    g,h,i = M[2]

    return [
        [ (e*i - f*h), -(b*i - c*h),  (b*f - c*e) ],
        [-(d*i - f*g),  (a*i - c*g), -(a*f - c*d)],
        [ (d*h - e*g), -(a*h - b*g),  (a*e - b*d)]
    ]

#  Inversa modular 3x3
def inversa_modular_3x3(M, mod=MOD):
    det = determinante_3x3(M) % mod
    inv_det = inverso_modular(det, mod)

    if inv_det is None:
        raise ValueError("La matriz no es invertible en módulo 27")

    adj = adjunta_3x3(M)
    
    inv = [
        [(adj[r][c] * inv_det) % mod for c in range(3)]
        for r in range(3)
    ]
    return inv


#  Multiplicación de matrices en mod 27
def mult_mod(A, B, mod=MOD):
    filas = len(A)
    columnas = len(B[0])
    inter = len(B)
    # crea una matriz de 0s
    R = [[0]*columnas for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            for k in range(inter):
                R[i][j] += A[i][k] * B[k][j]
            R[i][j] %= mod

    return R

#  Transponer
def transponer(M):
    return [list(col) for col in zip(*M)]

#  Conversión lista matriz y matriz→lista
def lista_a_matriz(L):
    return [L[i:i+3] for i in range(0, len(L), 3)]
# conversion matriz a lista
def matriz_a_lista(M):
    res = []
    for fila in M:
        res.extend(fila)
    return res
