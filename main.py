# Marcelo Huallpara Rodriguez Grupo 952 16 de Agosto de 2023
# Duplicados. Dada una lista de números enteros, retorna True si al menos un
# valor aparece dos veces, y Falso si todos los elementos son distintos.
# Ejemplos:
# nums = [1, 2, 3, 1]
# duplicados(nums)
# True

# nums = [1, 2, 3, 4]
# duplicados(nums)
# False

def duplicados(lista):
    s=set(lista)
    if len(s) >= len(lista):
        return True
    else:
        return False
    print(duplicados(lista=[15, 16, 17, 17, 18]))