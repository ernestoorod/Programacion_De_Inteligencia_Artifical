numero = 0
while numero<=0:
    numero = int(input("Dame un numero: "))
    if numero <=0:
        print("Numero no valido, usa un numero positivo")

# numero = 1
multiplicacion = 0
for i in range(1, 11):
    multiplicacion = numero * i
    print(f"{numero} * {i} = {multiplicacion}")