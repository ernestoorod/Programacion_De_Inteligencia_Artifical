# Tu solucion aqui
# Genera la secuencia de Fibonacci con los primeros 20 numeros
# Usa un bucle for y el método .append().

fibonacci = []

# Tu código aquí

for i in range(20):
    if i == 0:
        fibonacci.append(0)
    elif i == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

print(f"Primeros 20 números de Fibonacci: {fibonacci}")