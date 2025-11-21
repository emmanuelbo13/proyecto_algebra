# main.py
import string
from math import gcd
from methods import (
    inversa_modular_3x3,
    mult_mod,
    transponer,
    lista_a_matriz,
    matriz_a_lista,
    determinante_3x3
)

MOD = 27

mensaje = input("Escribe tu mensaje: ").lower()

alfabeto = list(string.ascii_lowercase) + [" "]


from math import gcd
from methods import lista_a_matriz, determinante_3x3

MOD = 27

# -------------------------
# Pedir clave 3×3 segura
# -------------------------
while True:
    entrada = input("Ingresa tu clave de 9 dígitos: ")

    # Validar que son 9 números
    if len(entrada) != 9 or not entrada.isdigit():
        print("Error: debes ingresar exactamente 9 dígitos.")
        continue

    # Convertir cada dígito a entero
    lista_digitos = [int(c) for c in entrada]

    # Convertir lista → matriz 3×3
    clave = lista_a_matriz(lista_digitos)

    # Calcular determinante mod 27
    det = determinante_3x3(clave) % MOD

    if gcd(det, MOD) != 1:
        print("Esa clave NO sirve (no es invertible en módulo 27). Prueba otra.")
        continue

    print("Clave válida e invertible.")
    break

# Convertir mensaje a índices
indices = [alfabeto.index(c) for c in mensaje]

# Rellenar con espacios para que sea múltiplo de 3
while len(indices) % 3 != 0:
    indices.append(alfabeto.index(' '))

# Convertir a matriz 3×N
matriz_mensaje = lista_a_matriz(indices)
matriz_mensaje = transponer(matriz_mensaje)

print("\nMatriz del mensaje:")
for f in matriz_mensaje:
    print(f)

# CIFRADO
cifrado = mult_mod(clave, matriz_mensaje, MOD)

print("\nMatriz cifrada:")
for f in cifrado:
    print(f)

lista_cifrada = matriz_a_lista(transponer(cifrado))
mensaje_cifrado = "".join(alfabeto[i] for i in lista_cifrada)

print("\nMensaje cifrado:")
print(mensaje_cifrado)

# DESCIFRADO
inv_clave = inversa_modular_3x3(clave, MOD)
print("\nInversa modular de la clave:")
for f in inv_clave:
    print(f)

# convertir lista cifrada a matriz 3×N
matriz_cifrada = lista_a_matriz(lista_cifrada)
matriz_cifrada = transponer(matriz_cifrada)

descifrado = mult_mod(inv_clave, matriz_cifrada, MOD)

print("\nMatriz descifrada:")
for f in descifrado:
    print(f)

lista_descifrada = matriz_a_lista(transponer(descifrado))
mensaje_descifrado = "".join(alfabeto[i] for i in lista_descifrada)

print("\nMensaje descifrado:")
print(mensaje_descifrado)
