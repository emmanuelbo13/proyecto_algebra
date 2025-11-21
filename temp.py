matriz_mensaje = [
    [12, 4, 26],
    [4, 13, 2],
    [0, 13, 19]
]

# Transponer la matriz: zip transpone filas y columnas con el operador * para desempaquetar las filas. 
print(list(zip(*matriz_mensaje)))