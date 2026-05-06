#10. **Conjunto de vocales en una frase**
 # Dada una frase (cadena de texto), crea un conjunto que contenga las vocales que aparecen en ella
 #  (sin distinguir mayúsculas/minúsculas). Muestra el conjunto resultante.

def vocales_en_frase(frase):
    vocales = set()
    for letra in frase:
        if letra.lower() in "aeiou":
            vocales.add(letra.lower())
    return vocales
# Ejemplo de uso
frase = "Hola Mundo"
resultado = vocales_en_frase(frase) 
print(resultado)

