"""
Escribir una función que reciba como parámetro una lista de números. El método debe
retornar una lista de booleanos, True si el número es divisible entre 5, False si es no
es divisible. Ejemplo: [10, 3, 5, 9, 15, 1] retorna [True, False, True, False, True, False]
"""

import pandas as pd


def to_divisible_5(listanumeros_5):
    # Primero se crea un DataFrame y la funcion de numeros para empezar a correr el codigo
    df = pd.DataFrame({'Numeros': listanumeros_5})

    # Se usa una funcion lambda para verificar si es divisible entre 5 o no
    df['EsDivisiblePor5'] = df['Numeros'].apply(lambda x: x % 5 == 0)

    # Se convierte en una lista de booleanos
    resultado = df['EsDivisiblePor5'].tolist()

    return resultado

# Se empieza a correr el codigo para verificar su funcionamiento
numbers = [10, 7, 3, 15, 5, 8]
results = to_divisible_5(numbers)
print(results)