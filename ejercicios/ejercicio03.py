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
# Ingresar el apellido
apellido = input("Ingrese el apellido: ")
# Ingresar la edad
edad = int(input("Ingrese la edad: "))

# Mostrar los datos en una sola línea
print(f"Nombre completo: {nombre} {apellido}, Edad: {edad}")