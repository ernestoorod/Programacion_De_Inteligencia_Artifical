# Escribe una funcion invertir_palabras(texto) que reciba un string y devuelva el mismo string pero con las palabras en orden inverso.
# Ejemplo: Hola mundo Python -> Python mundo Hola

# Tu solución aquí
def invertir_palabras(texto):
    
    palabras = texto.split()
    # invertidas = palabras[::-1] # --  Primera Solucion
    palabras.reverse()  # -- Segunda Solucion
    texto = " ".join(palabras) # o invertidas  si usamos la primera solucion
    return texto

# Prueba
print(invertir_palabras("Hola mundo Python"))
print(invertir_palabras("IA es el futuro"))