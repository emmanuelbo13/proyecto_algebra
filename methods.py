from copy import deepcopy

a = [
	[1, 2, 3],
	[4, 8, 3],
	[7, 2, 5]
	
]

b = [
	[1, 3, 2],
 	[3, 1, 5],
 	[4, 2, 7]
]
"""Hallar la determinante de una matriz 3x3"""
def password_validator(matriz):
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]

    det = (a*e*i + b*f*g + c*d*h) - (c*e*g + b*d*i + a*f*h)
    return det

# det_clave = password_validator(clave)
# print(f"Determinante de la matriz clave: {det_clave}")

"""Transponer una matriz"""
def transponer_matriz(matriz):
    matriz_transpuesta = list(map(list, zip(*matriz)))
    return matriz_transpuesta

"""Hallar la multiplicación de dos matrices 3xN y Nx3"""
def matrix_multiplication(matriz_a, matriz_b):
    # Inicializar la matriz resultado con ceros 
    result = [[0 for _ in range(len(matriz_b[0]))] for _ in range(len(matriz_a))]

    if len(matriz_a[0]) != len(matriz_b):
        raise ValueError("Número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")
    
    for row in range(len(matriz_a)):
        for col in range(len(matriz_b[0])):
            for i in range(len(matriz_b)):
                result[row][col] += matriz_a[row][i] * matriz_b[i][col]

    return result

resultado = matrix_multiplication(a, b)
print("Resultado de la multiplicación de matrices:")
for fila in resultado:
    print(fila)

"""Aplicar modulo 27 a cada elemento de la matriz"""
def modulo_27(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = matriz[i][j] % 27
    
    return matriz

matriz_mod27 = modulo_27(resultado)
print("Matriz después de aplicar módulo 27:") 
for fila in matriz_mod27:
    print(fila)

"""Convertir la matriz en una lista"""

def matriz_a_lista(matriz):
    lista = []
    for fila in matriz:
        lista.extend(fila)
    return lista

"""Funcion para el metodo gauss jordan"""
def gauss_jordan(matriz):
    # Implementación del método de Gauss-Jordan para encontrar la inversa de una matriz
    n = len(matriz)
    identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    for i in range(n):
        # Hacer que el elemento diagonal sea 1
        factor = matriz[i][i]
        if factor == 0:
            raise ValueError("La matriz no es invertible.")
        for j in range(n):
            matriz[i][j] /= factor
            identidad[i][j] /= factor

        # Hacer que los demás elementos en la columna sean 0
        for k in range(n):
            if k != i:
                factor = matriz[k][i]
                for j in range(n):
                    matriz[k][j] -= factor * matriz[i][j]
                    identidad[k][j] -= factor * identidad[i][j]

    return identidad



def pretty_mat(M):
    return "[" + "\n " + "\n ".join("[" + ", ".join(f"{x:10.6f}" for x in row) + "]" for row in M) + "\n]"

def gauss_jordan_steps(A):
    n = 3
    M = [ [float(x) for x in A[i]] + [1.0 if i==j else 0.0 for j in range(n)] for i in range(n) ]
    print("Matriz aumentada inicial [A | I]:")
    print(pretty_mat(M))
    print()

    for col in range(n):
        print(f"--- Paso para columna {col} (pivote en M[{col}][{col}]) ---")
        # 1) Si pivote = 0, buscar fila para intercambiar
        if abs(M[col][col]) < 1e-12:
            swap_row = None
            for r in range(col+1, n):
                if abs(M[r][col]) > 1e-12:
                    swap_row = r
                    break
            if swap_row is None:
                raise ValueError("La matriz no es invertible (no se encuentra pivote).")
            M[col], M[swap_row] = M[swap_row], M[col]
            print(f"Intercambio de filas: F{col} <-> F{swap_row}")
            print(pretty_mat(M))
            print()

        # 2) Normalizar fila del pivote
        pivote = M[col][col]
        print(f"Pivote actual = {pivote:.6f}; normalizando F{col} dividiéndola por {pivote:.6f}")
        M[col] = [x / pivote for x in M[col]]
        print(f"Después de normalizar F{col}:")
        print(pretty_mat(M))
        print()

        # 3) Hacer ceros en la columna para las demás filas
        for fila in range(n):
            if fila == col:
                continue
            factor = M[fila][col]
            if abs(factor) < 1e-12:
                continue
            print(f"Haciendo cero en M[{fila}][{col}] con operación: F{fila} = F{fila} - ({factor:.6f}) * F{col}")
            M[fila] = [ M[fila][j] - factor * M[col][j] for j in range(2*n) ]
            print(pretty_mat(M))
            print()

    inverse = [ row[n:] for row in M ]
    print("--- Inversa obtenida A^{-1} ---")
    print(pretty_mat(inverse))
    print()
    return inverse

def mat_mult(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)
    C = [[0.0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                C[i][j] += A[i][k]*B[k][j]
    return C

# Matriz de ejemplo (puedes cambiarla por la tuya)




# A = [[2, 1, 1],
#      [1, 3, 2],
#      [1, 0, 0]]

# n = 3
# M = [ [float(x) for x in A[i]] + [1.0 if i==j else 0.0 for j in range(n)] for i in range(n) ]

# for fila in M:
#     print(fila)
if __name__ == "__main__":
    A = [
    [2.0, 1.0, 1.0],
    [1.0, 3.0, 2.0],
    [1.0, 0.0, 0.0]
    ]

    invA = gauss_jordan_steps(A)

    # Verificación A * A^{-1} = I
    product = mat_mult(A, invA)
    print("--- Verificación: A * A^{-1} ---")
    print(pretty_mat(product))

    rounded = [[0 if abs(x) < 1e-9 else round(x,6) for x in row] for row in product]
    print("--- Verificación (redondeada) ---")
    print(pretty_mat(rounded))