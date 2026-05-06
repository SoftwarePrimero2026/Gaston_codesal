#3. **Intersección y unión de listas**Dadas dos listas de números, crea dos conjuntos a partir de ellas y muestra:
#   - Los elementos comunes (intersección).
#   - La unión de ambos conjuntos.

def interseccion_union(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    interseccion = conjunto1 .intersection (conjunto2)
    union = conjunto1 .union (conjunto2)
    
    return interseccion, union   
#ejemplo de uso 
lista1= [1, 2, 3, 4, 5]
lista2= [4, 5, 6, 7, 8]
interseccion, union = interseccion_union(lista1, lista2)
print("Intersección:", interseccion)
print("Unión:", union) 
