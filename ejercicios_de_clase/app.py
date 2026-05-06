
n= int( input("Ingrese la cantidad de productos: ") ) 
productos = []

for i in range(n):
    nombre = input("Ingrese el nombre: ")
    rubro = input("Ingrese el rubro: ")
    precio = float(input("Ingrese el precio: "))
    productos.append((nombre, rubro, precio))

    # ordenar por nombre y luego por precio 

productos.sort(key=lambda x: (x[0], x[2])) 

print("Productos ordenados: ")
for p in productos:
    print(f"Nombre: {p[0]}, Rubro: {p[1]}, Precio: {p[2]}") 