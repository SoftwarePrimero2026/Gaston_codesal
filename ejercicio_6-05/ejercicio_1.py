#1. **Eliminar duplicados de una lista**Dada una lista con elementos repetidos,
# crea un nuevo conjunto que contenga solo los elementos únicos. 
# Luego, conviértelo de nuevo a una lista y muéstrala.


# Lista con elementos repetidos
lista_con_duplicados = [1, 2, 3, 4, 2, 5, 1, 6, 3]

# Eliminar duplicados usando un conjunto
conjunto_unico = set(lista_con_duplicados)

# Convertir de nuevo a una lista
lista_sin_duplicados = list(conjunto_unico)

# Mostrar la lista sin duplicados
print("Lista sin duplicados:", lista_sin_duplicados) 

