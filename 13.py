# Ejercicio 3.1
# Crea una clase Estudiante con los siguientes atributos:

# nombre
# edad
# notas (lista de numeros)
# promedio (calculado automaticamente en init)
# Y los siguientes metodos:

# agregar_nota(nota): añade una nota a la lista y recalcula el promedio
# info(): devuelve un string con el nombre, edad y promedio
# esta_aprobado(): devuelve True si el promedio >= 5.0


class Estudiante: 

    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = list(notas)
        self.promedio = sum(notas) / len(notas) if self.notas else 0.0

    def agregar_nota(self, nota):
        self.notas.append(nota)
        self.promedio = sum(self.notas) / len(self.notas)

    def info(self):
        return f"Estudiante: {self.nombre} tiene {self.edad} años y estas notas: {self.notas}, tiene un promedio de: {self.promedio:.2f}"

    def esta_aprobado(self):
        if self.promedio >= 5.0:
            return True
        else:
            return False

# =============================================================
#   CÓDIGO DE PRUEBA (TESTS)
# =============================================================

# 1. Crear un estudiante con notas iniciales
print("--- Creando estudiante ---")
estudiante1 = Estudiante("Carlos Gómez", 20, [4.5, 5.0, 3.8])

# Probando el método info()
print(estudiante1.info())  # Debería mostrar promedio de 4.43

# Probando el método esta_aprobado()
print(f"¿Está aprobado?: {estudiante1.esta_aprobado()}")  # Debería ser False

# ------------------------------------------------------------

# 2. Agregar una nota para subir el promedio
print("\n--- Agregando una nueva nota ---")
estudiante1.agregar_nota(7.0)

# Ver el nuevo estado después de agregar la nota
print(f"Nuevas notas: {estudiante1.notas}")
print(estudiante1.info())  # El promedio debería haber subido a 5.08

# Volver a probar si está aprobado
print(f"¿Está aprobado ahora?: {estudiante1.esta_aprobado()}")  # Debería ser True

# ------------------------------------------------------------

# 3. Crear otro estudiante que ya está aprobado desde el inicio
print("\n--- Creando segundo estudiante ---")
estudiante2 = Estudiante("Ana López", 22, [6.0, 7.5, 8.0])
print(estudiante2.info())
print(f"¿Está aprobado?: {estudiante2.esta_aprobado()}")  # Debería ser True

# ------------------------------------------------------------