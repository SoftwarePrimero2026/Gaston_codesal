# Crear un funcion que se ingresen los datos de una persona, 
# de los cuales son obligatorios, apellido, nombre y edad (optativo), 
# pero ademas se debe contemplar y mostrar si se ingreso domicilio como kwargs 
# (se puede componer de calle, altura, piso, departamento, ciudad y provincia)

def datos_persona(apellido, nombre, edad=None, **kwargs):
    persona = {
        'apellido': apellido,
        'nombre': nombre,
    }
    if edad is not None:
        persona['edad'] = edad 
        

    #defino los campos del domicilio y filtro los kwargs para obtener solo los relacionados al domicilio
    campos_domicilio = ['calle', 'altura', 'piso', 'departamento', 'ciudad', 'provincia']
    #diccionario para guardar solo las claves y valores relacionados al domicilio
    domicilio_data = {k: v for k, v in kwargs.items() if k in campos_domicilio}
    
    if domicilio_data:
        persona['domicilio'] = domicilio_data
        print(" Domicilio ingresado")
    else:
        print("No se ingresó domicilio")
    
    return persona

# --- Ejemplos de uso ---
def formato_persona_simple(persona):
    print(f"{persona['nombre']} {persona['apellido']}")
    
    #  Una sola línea: edad solo si existe
    if 'edad' in persona:
        print(f"Edad: {persona['edad']} años")
    else:
        print("Edad no especificada")
    
    if 'domicilio' in persona:
        print(f"Domicilio: {persona['domicilio']}")
    print("-" * 30)


# Solo datos obligatorios
persona = datos_persona("García", "Lucía")
formato_persona_simple(persona)

print("-" * 40)

# Con domicilio completo
formato_persona_simple(datos_persona(
     "Pérez", "Carlos", 35,
     calle="Av. Corrientes",
     altura=1234,
     piso=3,
     departamento="B",
     ciudad="Buenos Aires",
     provincia="CABA"
 ))

 #Con domicilio parcial
formato_persona_simple(datos_persona(
     "López", "Ana", 22,
     calle="San Martín",
     ciudad="Córdoba",
     provincia="Córdoba"
 ))





