import string
from methods import password_validator, matrix_multiplication, modulo_27, transponer_matriz, matriz_a_lista

mensaje = "Mate musculos"
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

"""Agrupar en columnas de 3 letras"""
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
lista_de_matriz = matriz_a_lista(matriz_mod27)
print("\nLista de indices cifrados:")
print(lista_de_matriz)

"""Hallar indices de la lista cifrada en el alfabeto para obtener el mensaje cifrado"""
mensaje_cifrado = ''.join([letras_minusculas[i] for i in lista_de_matriz])
print("\nMensaje cifrado:")
print(mensaje_cifrado)

"""Convertir mensaje cifrado nuveamente a matriz"""
matriz_cifrada = matriz_mod27
