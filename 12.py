# Ejercicio 2.9¶
# Escribe un programa que:

# Cree un archivo registro.csv con datos de alumnos (nombre, edad, nota)
# Lo lea de vuelta y calcule la nota media
# Muestre el nombre del alumno con la mayor nota
# Usa el modulo csv.

import csv

# Tu solución aquí              

# Paso 1: Crear el archivo CSV con datos de alumnos
datos_alumnos = [
    ["Nombre", "Edad", "Nota"],
    ["Ana", 22, 8.5],
    ["Carlos", 24, 9.2],
    ["Beatriz", 21, 7.8],
    ["David", 23, 6.5],
    ["Elena", 22, 9.8],
]

# Escribe tu código aquí

with open("registro.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(datos_alumnos)

# Paso 2: Leer el CSV y calcular la nota media
# Escribe tu código aquí

notas = {}

with open("registro.csv", newline="", encoding="utf-8") as f:
    lector = csv.DictReader(f)

    for fila in lector:
        nombre = fila["Nombre"]
        nota = float(fila["Nota"])

        notas[nombre] = nota

    media = sum(notas.values()) / len(notas)
    print(f"\nLa nota media de la clase es: {media:.2f}")

# Paso 3: Encontrar el alumno con mayor nota
# Escribe tu código aquí

alumno_mayor = max(notas, key=lambda x: x[1])
mayor = max(notas.values())
print(f"\nEl alumno con la nota más alta es {alumno_mayor} con una nota de {mayor:.2f}")

print("\nListado de alumnos ordenados por nota (de mayor a menor):")
for notas in sorted(notas.items(), key=lambda x: x[1], reverse=True):
    print(f"{notas[0]}: {notas[1]:.2f}")