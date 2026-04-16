# Desarrollar un programa en Python que permita ingresar 2 numeros enteros.
# Una vez finalizada la carga, debe indicar por pantalla si son iguales y cual de los dos es mayor,
# utilizando operadores de comparacion.

# Pasos a seguir para resolver el ejercicio:

# Ingresar el primer numero.
# Ingresar el segundo numero.
# Comparar ambos valores.
# Informar si son iguales o cual es mayor.

# Salida esperada:
# Los numeros son iguales
# o
# El numero 9 es mayor que 4



# INICIO DE PROGRAMA PARA COMPARAR DOS NUMEROS ENTEROS 


# Ingresar los números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Proceso para comparar los valores
if num1 == num2:
    print("Los numeros son iguales")
elif num1 > num2:
    print(f"El numero {num1} es mayor que {num2}")
else:
    print(f"El numero {num2} es mayor que {num1}") 

