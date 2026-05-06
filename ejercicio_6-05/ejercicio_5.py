#5. **Lista de compras sin repeticiones**Dada una lista de productos (puede tener productos repetidos), 
# conviértela en un conjunto para eliminar duplicados. 
# Luego, muestra la lista única ordenada alfabéticamente.

def lista_compras_unica(productos):
    conjunto_productos = set(productos)
    lista_unica_ordenada = sorted(conjunto_productos)
    return lista_unica_ordenada 
# Ejemplo de uso    
lista_productos = ["leche", "pan", "huevos", "leche", "frutas", "pan"]
resultado = lista_compras_unica(lista_productos)
print(resultado)

