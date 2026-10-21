# Ejercicio 3.3
# Clase Tienda con métodos mágicos

# Crea una clase Tienda que gestione un catálogo de productos y demuestre el uso de múltiples métodos mágicos.

# Requisitos

# Clase Producto Cada producto tiene:

# nombre (str)
# precio (float)
# stock (int)
# Y debe implementar:

# __init__(nombre, precio, stock)
# __str__() → "Nombre: Precio€ (Stock: N)"
# __repr__() → Producto('Nombre', 9.99, 5)
# __bool__() → False si stock == 0, True en otro caso
# __mul__(self, cantidad) → devuelve un float (precio × cantidad)

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre}: {self.precio} € (Stock: {self.stock})"

    def __repr__(self):
        return f"Producto('{self.nombre}', {self.precio}, {self.stock})"

    def __bool__(self):
        return self.stock > 0

    def __mul__(self, cantidad):
        return float(self.precio * cantidad)

# Clase Tienda Gestiona una lista de productos. Debe implementar:

# Método mágico	Propósito	Operación
# __init__(nombre)	Inicializar tienda con nombre vacío	tienda = Tienda("MiTienda")
# __len__()	Devolver número de productos	len(tienda)
# __getitem__(index)	Acceder a un producto por índice	tienda[0]
# __iter__()	Recorrer productos con for	for p in tienda:
# __contains__(nombre)	Buscar producto por nombre	"Laptop" in tienda
# __str__()	Representación legible	print(tienda)
# __repr__()	Representación oficial	repr(tienda)
# __bool__()	False si tienda vacía	if tienda:
# __eq__(otra)	Comparar dos tiendas por número de productos	tienda1 == tienda2
# __format__(fmt)	Formateo personalizado	f"{tienda:inventario}"
# __add__(otra)	Combinar dos tiendas	tienda1 + tienda2
# __enter__() / __exit__()	Context manager	with Tienda("X") as t:

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self._productos = []

    def __getitem__(self, index):
        return self._productos[index]
    
    def __len__(self):
        return len(self._productos)

    def __iter__(self):
        return iter(self._productos)

    def __contains__(self, nombre):
        return any(l.nombre == nombre for l in self._productos)

    def __str__(self):
        return f"Tienda '{self.nombre}', ({len(self)} productos)"

    def __repr__(self):
        return f"Tienda('{self.nombre}', productos={len(self)})"

    def __bool__(self):
        return len(self._productos) > 0

    def __eq__(self,otra):
        if not isinstance(otra, Tienda):
            return NotImplemented
        return len(self) == len(otra)

    def __lt__(self,otra):
        if not isinstance(otra, Tienda):
            return NotImplemented
        return len(self) < len(otra)

    def __format__(self, fmt):
        if fmt == "inventario":
            items = ", ".join(p.nombre for p in self._productos)
            return f"[{self.nombre}: {items if items else 'Vacía'}]"
        return str(self)
    
    def __add__(self, otra):
        if not isinstance(otra, Tienda):
            return NotImplemented
        nueva_tienda = Tienda(f"{self.nombre} + {otra.nombre}")
        nueva_tienda._productos = self._productos + otra._productos
        return nueva_tienda

    def __enter__(self):
        print(f">>> Abriendo Tienda: {self.nombre}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"<<< Cerrando Tienda: {self.nombre}")
        return False

    def agregar(self, producto):
        self._productos.append(producto)
        
    def buscar(self, nombre):
        return next((l for l in self._productos if l.nombre == nombre), None)

    def total(self):
        return sum(l.precio * l.stock for l in self._productos)

# ==========================================
# BATERÍA DE PRUEBAS: CLASE TIENDA
# ==========================================
print("\n" + "="*50)
print("--- Iniciando pruebas de la clase Tienda ---")
print("="*50 + "\n")

# Crear algunos productos de ejemplo para las pruebas
p1 = Producto("Laptop Pro", 1299.99, 3)
p2 = Producto("Ratón Gamer", 29.99, 5)
p3 = Producto("Monitor 4K", 349.50, 2)

# 1. Prueba de __init__ y __bool__ (Tienda vacía)
print("1. Prueba de __init__ y __bool__ (Tienda vacía):")
tienda1 = Tienda("TecnoShop")
print(f"Tienda creada: '{tienda1.nombre}'")
print(f"¿Tiene productos la tienda? (bool): {bool(tienda1)}") 
# Esperado: False
print("-" * 40)

# Llenamos la tienda para las siguientes pruebas
tienda1.agregar(p1)
tienda1.agregar(p2)

# 2. Prueba de __bool__ (Tienda con productos) y __len__
print("2. Prueba de __bool__ y __len__ (Con productos):")
print(f"¿Tiene productos ahora?: {bool(tienda1)}") 
# Esperado: True
print(f"Número de productos en {tienda1.nombre}: {len(tienda1)}") 
# Esperado: 2
print("-" * 40)

# 3. Prueba de __getitem__ (Acceso por índice)
print("3. Prueba de __getitem__ (Acceso por índice):")
print(f"Primer producto: {tienda1[0]}") 
# Esperado: Laptop Pro: 1299.99 € (Stock: 3)
print(f"Segundo producto: {tienda1[1]}") 
# Esperado: Ratón Gamer: 29.99 € (Stock: 5)
print("-" * 40)

# 4. Prueba de __iter__ (Bucle for)
print("4. Prueba de __iter__ (Recorrer productos):")
print(f"Inventario completo de {tienda1.nombre}:")
for prod in tienda1:
    print(f" -> {prod}")
print("-" * 40)

# 5. Prueba de __contains__ (Operador in)
print("5. Prueba de __contains__ (Buscar por nombre):")
print(f"¿Está 'Laptop Pro' en la tienda?: {'Laptop Pro' in tienda1}") 
# Esperado: True
print(f"¿Está 'Auriculares' en la tienda?: {'Auriculares' in tienda1}") 
# Esperado: False
print("-" * 40)

# 6. Prueba de __str__ y __repr__
print("6. Prueba de __str__ y __repr__:")
print(f"Salida __str__: {tienda1}") 
# Esperado: Tienda 'TecnoShop', (2 productos)
print(f"Salida __repr__: {repr(tienda1)}") 
# Esperado: Tienda('TecnoShop', productos=2)
print("-" * 40)

# 7. Prueba de __format__ (Formateo personalizado 'inventario')
print("7. Prueba de __format__:")
print(f"Formato normal: {tienda1}")
print(f"Formato 'inventario': {tienda1:inventario}") 
# Esperado: [TecnoShop: Laptop Pro, Ratón Gamer]
tienda_vacia = Tienda("Outlet")
print(f"Formato 'inventario' (Vacía): {tienda_vacia:inventario}") 
# Esperado: [Outlet: Vacía]
print("-" * 40)

# 8. Prueba de __eq__ (Comparación de tiendas por cantidad de productos)
print("8. Prueba de __eq__ (Comparación ==):")
tienda2 = Tienda("GadgetZone")
tienda2.agregar(p3)
tienda2.agregar(Producto("Teclado Mecánico", 89.99, 2))

print(f"Tienda 1 ({len(tienda1)} productos) vs Tienda 2 ({len(tienda2)} productos)")
print(f"¿Tienen el mismo número de productos?: {tienda1 == tienda2}") 
# Esperado: True

print("Añadiendo un producto extra a Tienda 2...")
tienda2.agregar(Producto("Cable HDMI", 9.99, 10))
print(f"¿Siguen siendo iguales?: {tienda1 == tienda2}") 
# Esperado: False
print("-" * 40)

# 9. Prueba de __add__ (Combinar dos tiendas)
print("9. Prueba de __add__ (Fusión de tiendas con +):")
print(f"Fusionando '{tienda1.nombre}' y '{tienda2.nombre}'...")
tienda_fusionada = tienda1 + tienda2
print(f"Nueva tienda creada: {tienda_fusionada.nombre}")
# Esperado: TecnoShop + GadgetZone
print(f"Total productos en la nueva tienda: {len(tienda_fusionada)}") 
# Esperado: 5 (2 de tienda1 + 3 de tienda2)
print(f"Inventario fusionado: {tienda_fusionada:inventario}")
print("-" * 40)

# 10. Prueba de __enter__ y __exit__ (Context Manager / Bloque with)
print("10. Prueba de Context Manager (with):")
with Tienda("Tienda Temporal X") as t_temp:
    print(f"   [Dentro del bloque] Gestionando la tienda: {t_temp.nombre}")
    t_temp.agregar(p1)
    print(f"   [Dentro del bloque] Productos agregados: {len(t_temp)}")
# Aquí se debe imprimir automáticamente el mensaje de cierre al salir del bloque
print("-" * 40)

print("\n--- Batería de pruebas finalizada con éxito ---")