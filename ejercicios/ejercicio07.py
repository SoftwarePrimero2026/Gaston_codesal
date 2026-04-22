# Desarrollar un programa en Python que permita ingresar la edad de una persona.
# Una vez finalizada la carga, debe mostrar por pantalla si la persona es menor de edad,
# mayor de edad o adulto mayor.

# Pasos a seguir para resolver el ejercicio:

# Ingresar la edad de la persona.
# Evaluar la edad utilizando estructuras de decision.
# Mostrar el mensaje correspondiente.

# Salida esperada:
# Edad: 72
# Resultado: Es un adulto mayor



# INICIO DE PROGRAMA PARA EVALUAR LA EDAD DE UNA PERSONA

# Ingresar la edad
edad = int(input("Ingrese la edad de la persona: "))

# estructura de decisión para evaluar la edad
if edad < 18:
    categoria = "menor de edad"
elif edad < 65:
    categoria = "mayor de edad"
else:
    categoria = "adulto mayor"

# Mostrar resultado
print(f"Edad: {edad}")
print(f"Resultado: Es un {categoria}")
