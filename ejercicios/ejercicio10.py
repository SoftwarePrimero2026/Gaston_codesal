# Desarrollar un programa en Python que permita ingresar una palabra o una frase corta.
# Una vez finalizada la carga, debe mostrar por pantalla el texto original, el texto en mayusculas,
# el texto en minusculas y la cantidad total de caracteres.

# Pasos a seguir para resolver el ejercicio:

# Ingresar una palabra o frase corta.
# Mostrar el texto original.
# Mostrar el texto en mayusculas.
# Mostrar el texto en minusculas.
# Mostrar la cantidad de caracteres.

# Salida esperada:
# Texto original: Hola Mundo
# Mayusculas: HOLA MUNDO
# Minusculas: hola mundo
# Cantidad de caracteres: 10



# INICIO DE PROGRAMA PARA ANALIZAR TEXTO


# Ingreso de texto
texto = input("Ingrese una palabra o frase corta: ")

# Mostrar resultados
print(f"Texto original: {texto}")
print(f"Mayusculas: {texto.upper()}")
print(f"Minusculas: {texto.lower()}")
print(f"Cantidad de caracteres: {len(texto)}")
