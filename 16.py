# Ejercicio 8
# Dada la siguiente lista de numeros, usa list comprehensions para:

# Obtener solo los numeros primos (divisibles solo por 1 y si mismos)
# Crear un diccionario con {numero: raiz_cuadrada} para numeros > 5
# Crear un conjunto con los caracteres unicos de todas las palabras
# Filtrar palabras que empiecen por vocal y convertir a mayuscula

numeros = [2, 3, 5, 7, 11, 13, 14, 15, 17, 18, 19, 20, 21, 23]
palabras = ["ana", "elefante", "uva", "arbol", "oso", "perro", "higo", "óscar"]

# Números primos - LISTA

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = []

for n in numeros:
    if es_primo(n):
        primos.append(n)

print(f"Números primos: {primos}")

# {numero: raiz_cuadrada} para numeros > 5 - DICCIONARIO

raiz_cuadrada = {}

for n in numeros:
    if n > 5:
        raiz_cuadrada[n] = n**0.5

print(f"Diccionario con raíces cuadradas: {raiz_cuadrada}")

# Caracteres únicos de todas las palabras - CONJUNTO

caracteres_unicos = set()

for palabra in palabras:
    for letra in palabra:
        caracteres_unicos.add(letra)

print(f"Caracteres únicos: {caracteres_unicos}")

# Palabras que empiezan por vocal, en mayúscula - LISTA

palabras_vocal = []

for palabra in palabras:
    if palabra[0].lower() in "aeiouáéíóú":
        palabras_vocal.append(palabra.upper())

print(f"Palabras vocales: {palabras_vocal}")
