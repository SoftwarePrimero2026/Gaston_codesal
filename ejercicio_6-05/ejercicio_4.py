#4. **Teléfono de contactos**Crea un diccionario que almacene nombres de contactos como claves y números de teléfono como valores. 
# Agrega al menos 3 contactos, luego permite buscar un número ingresando el nombre del contacto.


def agregar_contacto(agenda, nombre, numero):
    agenda [nombre] = numero 
def buscar_contacto(agenda, nombre):
    return agenda.get(nombre, "Contacto no encontrado") 
# Ejemplo de uso
agenda = {} 
agregar_contacto(agenda, "Alice", "123-456-7890")   
agregar_contacto(agenda, "Bob", "987-654-3210")
agregar_contacto(agenda, "Charlie", "555-555-5555") 
nombre_buscar = "Bob"
numero = buscar_contacto(agenda, nombre_buscar)     
print(f"El número de {nombre_buscar} es: {numero}")
nombre_buscar = "David"
numero = buscar_contacto(agenda, nombre_buscar)         
print(f"El número de {nombre_buscar} es: {numero}")

