# Dado un texto, escribe un programa que cuente cuantas veces aparece cada palabra (sin distincion de mayúsculas/minúsculas). 
# Devuelve un diccionario con las frecuencias.
# Ejemplo: Hola hola Hola -> hola: 3


# Tu solución aquí
texto = "Hola hola Hola Python python PYTHON"

print(f"Texto original: {texto}")

# Escribe tu código aquí

palabras = texto.lower().split()

print(f"Palabras formateadas: {palabras}")

frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

# Muestra el resultado

print(f"Frecuencia de palabras en texto: {frecuencia}")


