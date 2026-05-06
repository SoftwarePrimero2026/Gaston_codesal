#2. **Conteo de frecuencias**Dada una lista de palabras,
# crea un diccionario donde las claves sean las palabras y los valores sean el número de veces que aparecen en la lista.

def contar_frecuencias(palabras):
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias 
# Ejemplo de uso
lista_palabras = ["manzana", "banana", "manzana", "naranja", "banana", "manzana"]
resultado = contar_frecuencias(lista_palabras)
print(resultado) 
    