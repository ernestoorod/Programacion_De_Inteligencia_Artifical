numeros = [4, 7, 12, -3, 0]

for n in numeros:
    resultado = "nulo" if n == 0 else ("par" if n % 2 == 0 else "impar")    
    print(f"{n} -> {resultado}")
