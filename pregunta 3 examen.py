"""
Escribir una función que reciba como parámetro una lista de números, y retorne una tupla. El primer
elemento de la tupla es la cantidad de números sin repetir de la lista, el segundo elemento de la tupla
es la cantidad de números repetidos. Ejemplo: [1, 3, 1, 4, 5, 3, 7], resultado (3, 4).
Ejemplo dos: [1, 3, 1, 1, 3, 4] , resultado (1, 5). Nota: Puede usar el método Count de las listas.
Recibe de parámetro  el elemento que se desea contar.
"""

import pandas as pd

def count_repetidos_y_no_repetidos(lista_numeros):
    # Crear un DataFrame de pandas a partir de la lista de números
    df = pd.DataFrame({'Numeros': lista_numeros})

    # Contar la cantidad de veces que cada número aparece en la lista
    conteo = df['Numeros'].value_counts()

    # Calcular la cantidad de números no repetidos
    numeros_no_repetidos = len(conteo[conteo == 1])

    # Calcular la cantidad de números repetidos
    numeros_repetidos = len(conteo) - numeros_no_repetidos

    return (numeros_no_repetidos, numeros_repetidos)


# Ejemplos de uso
lista1 = [1, 3, 1, 4, 5, 3, 7]
resultado1 = count_repetidos_y_no_repetidos(lista1)
print(resultado1)  # Debería imprimir (3, 4)

lista2 = [1, 3, 1, 1, 3, 4]
resultado2 = count_repetidos_y_no_repetidos(lista2)
print(resultado2)  # Debería imprimir (1, 5)