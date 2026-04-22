# Desarrollar un programa en Python que permita ingresar el nombre de 5 productos.
# Una vez finalizada la carga, debe mostrar por pantalla la lista completa de productos,
# numerada y con un formato claro.

# Pasos a seguir para resolver el ejercicio:

# Ingresar 5 nombres de productos.
# Guardar cada producto en una lista.
# Mostrar la lista numerada.

# Salida esperada:
# 1. Arroz
# 2. Fideos
# 3. Leche
# 4. Pan
# 5. Azucar



# INICIO DE PROGRAMA PARA INGRESAR Y MOSTRAR 5 PRODUCTOS

# Crear lista vacía
productos = []

# Ingresar 5 productos
print("Ingrese 5 nombres de productos:")
for i in range(5):
    producto = input(f"Producto {i+1}: ")
    productos.append(producto)

# Mostrar lista numerada
print("\nLista de productos:")
for i in range(len(productos)):
    print(f"{i+1}. {productos[i]}")
