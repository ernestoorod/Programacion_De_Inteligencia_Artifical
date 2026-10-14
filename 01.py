# Calculadora de descuentos

precio_articulo = float(input("Dime el precio del articulo: "))
descuento = float(input("Dime de cuanto es el descuento: "))

precio_final = precio_articulo * (1 - descuento / 100)

if descuento == 0:
    clasificacion_descuento = "Sin descuento"
elif descuento >= 1 and descuento <= 15:
    clasificacion_descuento = "Oferta"
elif descuento >= 16 and descuento <= 40:
    clasificacion_descuento = "Gran oferta"
else:
    clasificacion_descuento = "Liquidación"
 

print(f"El precio final del producto es: {precio_final:.2f} y se ha aplicado el descuento: {clasificacion_descuento}")