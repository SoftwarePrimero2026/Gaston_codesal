# Desarrollar un programa en Python que permita ingresar 2 numeros enteros.
# Una vez finalizada la carga, debe mostrar por pantalla el resultado de la suma, la resta,
# la multiplicacion y la division entre ambos numeros.

# Pasos a seguir para resolver el ejercicio:

# Ingresar el primer numero.
# Ingresar el segundo numero.
# Mostrar el resultado de las operaciones basicas.

# Salida esperada:
# Suma: 15
# Resta: 5
# Multiplicacion: 50
# Division: 2.0



# INICIO DE PROGRAMA 

# Programa para realizar operaciones básicas con 2 números enteros

# Ingreso para los números 
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Calcular las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

# Mostrar los resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multiplicacion}")
print(f"Division: {division}")