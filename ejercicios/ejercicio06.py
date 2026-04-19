# Desarrollar un programa en Python que permita ingresar la nota de un alumno.
# Una vez finalizada la carga, debe mostrar por pantalla si la condicion del alumno es:
# Excelente, Muy bien, Bien, Regular o Insuficiente.

# Pasos a seguir para resolver el ejercicio:

# Ingresar la nota del alumno.
# Evaluar la nota con estructuras de decision.
# Mostrar la condicion correspondiente.

# Salida esperada:
# Nota: 8
# Condicion: Muy bien



# INICIO DE PROGRAMA PARA EVALUAR LA NOTA DE UN ALUMNO


# Ingresar la nota
nota = int(input("Ingrese la nota del alumno (0-10): "))

# Evaluar la condición
if nota >= 9:
    condicion = "Excelente"
elif nota >= 7:
    condicion = "Muy bien"
elif nota >= 5:
    condicion = "Bien"
elif nota >= 3:
    condicion = "Regular"
else:
    condicion = "Insuficiente"

# Mostrar resultado
print(f"Nota: {nota}")
print(f"Condicion: {condicion}")
