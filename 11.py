# Ejercicio 2.8
# Escribe una funcion procesar_lista(lista) que reciba una lista de elementos y:

# Sumar todos los números (ignora los que no sean numéricos)
# Si hay un valor negativo, lanzar una ValueError
# Si la lista está vacía, lanzar un ValueError
# Devolver la suma total
# Prueba con diferentes listas.

def procesar_lista(lista):
    if not lista:
        raise ValueError("La lista está vacía")

    suma = 0
    for elemento in lista:
        if isinstance(elemento, (int, float)) and not isinstance(elemento, bool):
            if elemento < 0:
                raise ValueError("Se encontró un valor negativo")
            suma += elemento
    return suma


pruebas = [
    [1, 2, 3, "hola", 4],
    [10, 20, 30],
    [1.5, 2.5, None, "x"],
    [True, 5, 3],
    [-1, 2, 3],
    [],
]

for lista in pruebas:
    try:
        print(f"{lista} -> {procesar_lista(lista)}")
    except ValueError as e:
        print(f"{lista} -> Error: {e}")