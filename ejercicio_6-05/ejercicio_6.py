#6. **Invertir claves y valores**Dado un diccionario donde las claves y los valores son únicos, 
# crea un nuevo diccionario que intercambie claves por valores. Por ejemplo: `{"a": 1, "b": 2}` → `{1: "a", 2: "b"}`.

def invertir_diccionario(diccionario):
    diccionario_invertido = {valor: clave for clave, valor in diccionario.items()}
    return diccionario_invertido 
# Ejemplo de uso
diccionario_original = {"a": 1, "b": 2, "c": 3}
diccionario_invertido = invertir_diccionario(diccionario_original)  
print(diccionario_invertido) 