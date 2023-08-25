"""
Marcelo Huallpara Rodriguez Grupo 952 16 de Agosto de 2023
Estadística Básica. Cree una clase llamada Estadística que contiene como atributo una lista
de números naturales la cual puede contener repetidos. Debe contener los siguientes métodos:
A. Frecuencia de Números. Dada la lista, devuelve un diccionario con el número de veces que
aparece cada número en la lista.
B. Moda. Dada la lista, devuelva la moda de la lista (el valor más repetido). Puedes usar la
función anterior como ayuda.
C. Histograma. Dada la lista, muestra el histograma de la lista. Puedes reusar los métodos
anteriores.
Ejemplo:
lista = ListaNumeros ([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])
lista.histograma()

Salida:
1 *****
2 ******
3 ****
4 **
"""
class Estadística:
    def __init__(self, listnumbers):
        self.listnumbers = listnumbers

    def frecuencia_numeros(self):
        frequency = {}
        for num in self.listnumbers:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        return frequency

    def moda(self):
        frequency = self.frecuencia_numeros()
        moda = max(frequency, key=frequency.get)
        return moda

    def histograma(self):
        frequency = self.frecuencia_numeros()
        for num, count in frequency.items():
            print(f"{num} {'*' * count}")

numeros = [1, 2, 2, 4, 3, 2, 3, 4, 4, 2, 1, 1, 2, 1, 1, 3, 1]
estadistica = Estadística(numeros)
estadistica.histograma()


