# Bebe si edad < 2
# Niño si 2 <= edad < 13
# Adolescente si 13 <= edad < 18
# Adulto si 18 <= edad < 65
# Adulto mayor si edad >= 65


def clasificar_edad(edad):
    if edad < 2:
        return "Bebe"
    elif edad <= 2 and edad < 13:
        return  "Niño"
    elif edad <= 13 and edad < 18:
        return  "Adolescente"
    elif edad <= 18 and edad < 65:
        return "Adulto"
    else:
        return "Adulto mayor"

for edad in [1, 5, 15, 25, 70]:
    print(f"{edad} años -> {clasificar_edad(edad)}")