"""
Marcelo Huallpara Rodriguez Grupo 952 16 de Agosto de 2023
Duplicados. Dada una lista de números enteros, retorna True si al menos un
valor aparece dos veces, y Falso si todos los elementos son distintos.
Ejemplos:
nums = [1, 2, 3, 1]
duplicados(nums)
True

nums = [1, 2, 3, 4]
duplicados(nums)
False
"""

def duplicados(numeros):
    numero_set = set()
    for numero in numeros:
        if numero in numero_set:
            return True
        numero_set.add(numero)
    return False

numeros1 = [1, 2, 3, 4, 5, 6, 7]
resultado1 = duplicados(numeros1)
print(resultado1)

numeros2 = [1, 2, 3, 3, 7, 4, 7]
resultado2 = duplicados(numeros2)
print(resultado2)