# Desarrollar un programa en Python que permita ingresar numeros enteros hasta que el usuario ingrese 0.
# Una vez finalizada la carga, debe mostrar por pantalla la cantidad de numeros ingresados y la suma total.

# Pasos a seguir para resolver el ejercicio:

# Solicitar un numero al usuario.
# Repetir el pedido hasta que el usuario ingrese 0.
# Acumular la suma de los numeros ingresados.
# Contar cuantos numeros fueron ingresados.

# Salida esperada:
# Cantidad de numeros ingresados: 4
# Suma total: 28



# INICIO DE PROGRAMA PARA SUMAR NUMEROS HASTA INGRESAR 0

# Declarar variables para la suma y el contador
suma = 0
contador = 0

# Leer números hasta ingresar 0
print("Ingrese números enteros (0 para terminar):")
numero = int(input())

while numero != 0:
    suma += numero
    contador += 1
    numero = int(input())

# Mostrar resultados
print(f"Cantidad de numeros ingresados: {contador}")
print(f"Suma total: {suma}")
