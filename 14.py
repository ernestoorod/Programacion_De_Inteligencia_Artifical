# Ejercicio 3.2
# Crea una clase CuentaBancaria con:

# Atributos: titular (string), saldo (float)
# Metodos:
# __init__(titular, saldo=0.0): inicializa con saldo opcional
# depositar(monto): anade dinero a la cuenta
# retirar(monto): quita dinero (si hay suficiente)
# __str__(): devuelve f"Cuenta de {titular}: {saldo:.2f} Euros"
# __add__(otra_cuenta): devuelve una nueva cuenta con la suma de saldos

class CuentaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0):
        self.titular = titular
        self.saldo = float(saldo)

    def depositar(self, monto: float):
        if monto > 0:
            self.saldo += monto
            print(f"Se han depositado {monto:.2f} Euros en la cuenta de {self.titular}.")
        else:
            print("El monto a depositar debe ser mayor que cero.")

    def retirar(self, monto: float):
        if monto > self.saldo:
            print(f"Fondos insuficientes en la cuenta de {self.titular} para retirar {monto:.2f} Euros.")
        elif monto <= 0:
            print("El monto a retirar debe ser mayor que cero.")
        else:
            self.saldo -= monto
            print(f"Se han retirado {monto:.2f} Euros de la cuenta de {self.titular}.")

    def __str__(self):
        return f"Cuenta de {self.titular}: {self.saldo:.2f} Euros"

    def __add__(self, otra_cuenta):
        if isinstance(otra_cuenta, CuentaBancaria):
            nuevo_titular = f"Conjunta ({self.titular} y {otra_cuenta.titular})"
            nuevo_saldo = self.saldo + otra_cuenta.saldo
            return CuentaBancaria(nuevo_titular, nuevo_saldo)
        return NotImplemented


# --- PRUEBAS Y OPERACIONES ---

# 1. Crear dos cuentas bancarias
cuenta1 = CuentaBancaria("Carlos", 1500.50)
cuenta2 = CuentaBancaria("Ana", 500.00)

print("--- Estado Inicial ---")
print(cuenta1)
print(cuenta2)
print()

# 2. Realizar operaciones en la cuenta 1
print("--- Operaciones Cuenta 1 (Carlos) ---")
cuenta1.depositar(200.00)
cuenta1.retirar(100.50)
cuenta1.retirar(2000.00)  # Intento de retiro mayor al saldo
print(cuenta1)
print()

# 3. Realizar operaciones en la cuenta 2
print("--- Operaciones Cuenta 2 (Ana) ---")
cuenta2.depositar(500.00)
cuenta2.retirar(300.00)
print(cuenta2)
print()

# 4. Sumar ambas cuentas utilizando el método mágico __add__
print("--- Fusión de Cuentas (__add__) ---")
cuenta_conjunta = cuenta1 + cuenta2
print(cuenta_conjunta)