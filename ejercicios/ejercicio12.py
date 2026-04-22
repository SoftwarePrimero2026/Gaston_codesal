# Desarrollar un programa en Python que permita registrar nombres y edades de alumnos hasta que el usuario escriba "salir".
# Una vez finalizada la carga, debe mostrar por pantalla la lista completa de alumnos ingresados,
# indicando nombre, edad y la cantidad total de alumnos mayores o iguales a 18 anos.

# Pasos a seguir para resolver el ejercicio:

# Solicitar el nombre del alumno.
# Si el nombre es distinto de "salir", solicitar la edad.
# Guardar los datos del alumno.
# Repetir el proceso hasta ingresar "salir".
# Mostrar la lista de alumnos cargados.
# Mostrar la cantidad de alumnos mayores o iguales a 18 anos.

# Salida esperada:
# 1. Nombre: Ana, Edad: 17
# 2. Nombre: Pedro, Edad: 20
# 3. Nombre: Lucia, Edad: 18
# Total de alumnos mayores o iguales a 18 anos: 2



# INICIO DE PROGRAMA PARA REGISTRAR ALUMNOS HASTA "SALIR"

# Creacion de listas para almacenar los datos
alumnos = []
mayores_18 = 0

# Carga de datos
print("Ingrese nombres de alumnos (escriba 'salir' para terminar):")
nombre = input("Nombre: ")

# Mientras el nombre no sea "salir", se solicita la edad y se guardan los datos
while nombre.lower() != "salir":
    edad = int(input("Edad: "))
    alumnos.append((nombre, edad))
# Contar cuantos alumnos son mayores o iguales a 18 anos    
    if edad >= 18:
        mayores_18 += 1
    
    nombre = input("Nombre: ")

# Mostrar resultados
print("\nLista de alumnos:")
for i, (nom, ed) in enumerate(alumnos, 1):
    print(f"{i}. Nombre: {nom}, Edad: {ed}")

print(f"Total de alumnos mayores o iguales a 18 anos: {mayores_18}")
