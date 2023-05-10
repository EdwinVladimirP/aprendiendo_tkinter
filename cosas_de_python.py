genero = input("Ingresa el Género M ó F: ")
edad = input("Ingresa la edad: ")
try:
    edad = int(edad)
except:
    print("Introduce la edad valida")
    exit()

if genero == "M":
    if edad >= 60:
        print("Ya se cumple la edad")
    else:
        print("Aún no se cumple la edad. ")
elif genero == "F":
    if edad >= 45:
        print("Ys se cumple la edad")
    else:
        print("Aún no se cumple la edad. ")
else:
    print("Digite una opción válida en el genero")