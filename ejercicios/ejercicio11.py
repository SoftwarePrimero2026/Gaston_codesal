# Desarrollar un programa en Python que permita ingresar la edad de una persona y si posee carnet de estudiante.
# Una vez finalizada la carga, debe mostrar por pantalla si puede acceder a un descuento,
# considerando que el descuento se aplica solo si es mayor o igual a 18 anos y tiene carnet.

# Pasos a seguir para resolver el ejercicio:

# Ingresar la edad de la persona.
# Ingresar si posee carnet de estudiante.
# Evaluar ambas condiciones utilizando operadores logicos.
# Mostrar si accede o no al descuento.

# Salida esperada:
# Edad: 20
# Carnet: si
# Resultado: Accede al descuento



# INICIO DE PROGRAMA PARA EVALUAR DESCUENTO POR EDAD Y CARNET DE ESTUDIANTE


# Ingresar datos
edad = int(input("Ingrese la edad: "))
carnet = input("¿Posee carnet de estudiante? (si/no): ").lower()

# Evaluar condiciones
tiene_descuento = (edad >= 18) and (carnet == "si")

# Mostrar resultado
print(f"Edad: {edad}")
print(f"Carnet: {carnet.title()}")
if tiene_descuento:
    print("Resultado: Accede al descuento")
else:
    print("Resultado: No accede al descuento")
