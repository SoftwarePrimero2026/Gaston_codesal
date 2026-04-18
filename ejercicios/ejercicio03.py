# Desarrollar un programa en Python que permita ingresar el nombre, el apellido y la edad de una persona.
# Una vez finalizada la carga, debe mostrar por pantalla un mensaje con todos los datos en una sola linea
# utilizando un formato claro.

# Pasos a seguir para resolver el ejercicio:

# Ingresar el nombre de la persona.
# Ingresar el apellido de la persona.
# Ingresar la edad de la persona.

# Salida esperada:
# Nombre completo: Juan Perez, Edad: 30



# INICIO DE PROGRAMA 
# Programa sencillo para ingresar y mostrar datos de una persona

# Ingresar el nombre
nombre = input("Ingrese el nombre: ")
#tratamiento de error para el nombre 
try:
    if not nombre.isalpha():
        raise ValueError("El nombre debe contener solo letras.")
except ValueError as e:
    print(e)
# Ingresar el apellido
apellido = input("Ingrese el apellido: ")
#tratamiento de error para el apellido
try:
    if not apellido.isalpha():
        raise ValueError("El apellido debe contener solo letras.")
except ValueError as e:
    print(e)
# Ingresar la edad
edad = int(input("Ingrese la edad: "))
#tratamiento de error para la edad
try:
    if edad < 0:
        raise ValueError("La edad debe ser un número positivo.")
except ValueError as e:
    print(e)

# Mostrar los datos en una sola línea
print(f"Nombre completo: {nombre} {apellido}, Edad: {edad}")