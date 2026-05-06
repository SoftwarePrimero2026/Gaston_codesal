#8. **Lista de diccionarios**Define una lista de diccionarios que representen personas con las claves `"nombre"` y `"edad"`. 
# Escribe un programa que filtre y muestre solo las personas mayores de 18 años.

def filtrar_mayores(lista_personas):
    mayores = [persona for persona in lista_personas if persona["edad"] > 18]
    return mayores  
# Ejemplo de uso
personas = [
    {"nombre": "Alice", "edad": 30},        
    {"nombre": "Bob", "edad": 17},
    {"nombre": "Charlie", "edad": 25},
    {"nombre": "David", "edad": 15}
]
resultado = filtrar_mayores(personas)
print(resultado)
