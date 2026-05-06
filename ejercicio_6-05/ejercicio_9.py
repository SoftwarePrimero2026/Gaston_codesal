#9. **Eliminar valores None de un diccionario**Dado un diccionario que puede contener valores `None`,
#  elimina todos los pares cuyo valor sea `None` y devuelve el diccionario limpio.

def eliminar_none(diccionario): 
    diccionario_limpio = {clave: valor for clave, valor in diccionario.items() if valor is not None}
    return diccionario_limpio   
# Ejemplo de uso
diccionario = {
    "nombre": "Alice",
    "edad": 30,
    "ciudad": None,
    "profesion": "Ingeniera",
    "hobby": None
}
resultado = eliminar_none(diccionario)
print(resultado)

