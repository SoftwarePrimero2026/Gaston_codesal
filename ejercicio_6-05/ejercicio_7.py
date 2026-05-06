#7. **Diferencia simétrica**Crea dos conjuntos con números enteros. 
# Encuentra los elementos que están en uno u otro conjunto, pero no en ambos (diferencia simétrica).

def diferencia_simetrica(conjunto1, conjunto2):
    diferencia = conjunto1.symmetric_difference(conjunto2)
    return diferencia   
# Ejemplo de uso
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
resultado = diferencia_simetrica(conjunto1, conjunto2)
print("Diferencia simétrica:", resultado)
