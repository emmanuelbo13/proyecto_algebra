import string
from methods import gauss_jordan, lista_a_matriz, password_validator, matrix_multiplication, modulo_27, transponer_matriz, matriz_a_lista

mensaje = "kelly pero que monda"
mensaje = mensaje.lower()
print(f"Mensaje en minusculas: {mensaje}")
print("Longitud del mensaje:", len(mensaje))

"""lista del alfabeto: A-Z : indices 0 al 25 - añadir espacio en posicion indice 26""" 
letras_minusculas = list(string.ascii_lowercase)  
letras_minusculas.append(' ') 

#print(len(letras_minusculas))
print(letras_minusculas)

# remplazar por user input
clave = [
	[35, 53, 12],
 	[12, 21, 5],
 	[2, 4, 1]
]

print(len(clave))
""""Comprobar que la matriz tiene determinante distinto de cero"""
det_clave = password_validator(clave)
if det_clave == 0:
    raise ValueError("La matriz clave tiene determinante cero, no es invertible.")
else:
	print("Contraseña aceptada.")


"""Obtener los índices de cada letra en mensaje
	Con la misma logica: se crea una lista de indices para todo el mensaje """ 
# print(letras_minusculas.index('a'))  # Debería imprimir 0

indices = [letras_minusculas.index(c) for c in mensaje]
# print(f"indices: {indices}") 

"""La matriz debe tener 3 filas, por lo que el número total de elementos
debe ser múltiplo de 3. Si no lo es, se rellenan con espacios"""
if len(indices) % 3 != 0:
	# Rellenar con espacios si faltan para completar un múltiplo de 3
	while len(indices) % 3 != 0:
		indices.append(letras_minusculas.index(' '))

print(f"indices despues de rellenar: {indices}")

"""Convertir la lista de índices en una matriz de 3 filas"""
matriz_mensaje = []
for i in range(0, len(indices), 3):
	matriz_mensaje.append(indices[i:i+3])

print("matriz_mensaje:")
for fila in matriz_mensaje:
	print(fila)

"""Transponer para obtener matriz 3x7
desempaquetar las filas con el operador* y usar zip para transponer, y luego convertir tuplas a listas, 
y finalmente meter todas las listas en una lista mayor"""

matriz_mensaje = transponer_matriz(matriz_mensaje)
print("\nmatriz_mensaje:")
for fila in matriz_mensaje:
	print(fila)

"""Multiplicar la matriz clave por la matriz mensaje"""
resultado = matrix_multiplication(clave, matriz_mensaje)
print("\nResultado de la multiplicación de matrices:")
for fila in resultado:
    print(fila)

"""Aplicar modulo 27 a cada elemento de la matriz"""
matriz_mod27 = modulo_27(resultado)
print("\nMatriz después de aplicar módulo 27:")
for fila in matriz_mod27:
    print(fila)

"""Transponer la matriz resultando y convertirla en una lista"""
matriz_mod27 = transponer_matriz(matriz_mod27)
lista_cifrada = matriz_a_lista(matriz_mod27)
print("\nLista de indices cifrados:")
print(lista_cifrada)

"""Hallar indices de la lista cifrada en el alfabeto para obtener el mensaje cifrado"""
mensaje_cifrado = ''.join([letras_minusculas[i] for i in lista_cifrada])
print("\nMensaje cifrado:")
print(mensaje_cifrado)

"""Convertir mensaje cifrado nuveamente a matriz"""
matriz_cifrada = lista_a_matriz(lista_cifrada)
matriz_cifrada = transponer_matriz(matriz_cifrada)
print("\nMatriz cifrada:")
for fila in matriz_cifrada:
	print(fila)

"""Hallar la inversa de la matriz clave usando Gauss Jordan"""
inversa_clave = gauss_jordan(clave)
print("\nMatriz inversa de la clave:")
for fila in inversa_clave:
    print(fila)

"""Aplicar el modulo 27 a la inversa de la clave """
inversa_clave_mod27 = modulo_27(inversa_clave)
print("\nMatriz inversa de la clave después de aplicar módulo 27:")
for fila in inversa_clave_mod27:
    print(fila)

"""Multiplicar la inversa de la clave por la matriz cifrada"""
resultado_descifrado = matrix_multiplication(inversa_clave_mod27, matriz_cifrada)
print("\nResultado de la multiplicación de la inversa de la clave por la matriz cifrada:")
for fila in resultado_descifrado:
	print(fila)

"""Aplicar modulo 27 a cada elemento de la matriz descifrada"""
matriz_descifrada_mod27 = modulo_27(resultado_descifrado)
print("\nMatriz descifrada después de aplicar módulo 27:")
for fila in matriz_descifrada_mod27:
    print(fila)

"""Transponer la matriz descifrada y convertirla en una lista"""
matriz_descifrada_mod27 = transponer_matriz(matriz_descifrada_mod27)
lista_descifrada = matriz_a_lista(matriz_descifrada_mod27)
print("\nLista de indices descifrados:")
print(lista_descifrada)

"""Hallar indices de la lista descifrada en el alfabeto para obtener el mensaje descifrado"""
"""Convertir float a int al numero mas cercano"""
lista_descifrada = [int(round(i)) for i in lista_descifrada]
#lista_descifrada = [(int(round(i))) % 27 for i in lista_descifrada]
# print(lista_descifrada)
mensaje_descifrado = ''.join([letras_minusculas[i] for i in lista_descifrada])
print("\nMensaje descifrado:")
print(mensaje_descifrado)

# for i in lista_cifrada:
# 	print(type(i))