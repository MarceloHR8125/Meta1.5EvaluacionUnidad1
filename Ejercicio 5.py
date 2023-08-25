"""
Marcelo Huallpara Rodriguez Grupo 952 16 de Agosto de 2023
Gestión de Pensionistas. Crear una clase llamada GrupoPensionistas la cual tendrá un
único atributo una lista o diccionario de objetos de tipo Pensionista (Elija a conveniencia
si una lista o diccionario). Cada objeto de Pensionista tiene los siguientes atributos:
identificador del pensionista (string), un entero que indica la edad y una serie de gastos
mensuales que se guardan (lista de enteros). El número de gastos mensuales puede variar entre
pensionistas. Por ejemplo, el pensionista con identificador '1111A' se llama 'Carlos' tiene 68
años y tiene 3 gastos mensuales de 640, 589 y 573.
La clase GrupoPensionistas debe tener los siguientes métodos:

a. mediaGastos(identificador) , dado el identificador o índice de un pensionista, devuelva el promedio de los gastos.
b. mediaEdad(), dado todos los pensionados, devuelve el promedio de las edades.
c. edadesExtremas(), dado todos los pensionados, devuelva al pensionado con menor y mayor edad en una tupla.
d. sumaPromedio(), dado todos los pensionados, devuelva la suma del promedio de los gastos de todos los pensionistas
de la lista.
e. mediaMaxima(), dado todos los pensionistas, retorne el mayor promedio de los gastos entre todos los pensionistas de
la lista, su nombre e identificador.
f. gastoPromedio(lst), dado todos los pensionistas, devuelve una lista con el gasto promedio de cada persona. La lista
resultante debe estar ordenada de forma ascendente.
"""

class Pensionista:
    def __init__(self, identificador, edad, gastos_mensuales):
        self.identificador = identificador
        self.edad = edad
        self.gastos_mensuales = gastos_mensuales

class GrupoPensionistas:
    def __init__(self):
        self.pensionistas = []

    def agregar_pensionista(self, pensionista):
        self.pensionistas.append(pensionista)

    def mediaGastos(self, identificador):
        for pensionista in self.pensionistas:
            if pensionista.identificador == identificador:
                total_gastos = sum(pensionista.gastos_mensuales)
                return total_gastos / len(pensionista.gastos_mensuales)
        return None

    def mediaEdad(self):
        total_edades = sum(p.edad for p in self.pensionistas)
        return total_edades / len(self.pensionistas)

    def edadesExtremas(self):
        pensionistas_sorted_by_age = sorted(self.pensionistas, key=lambda p: p.edad)
        return pensionistas_sorted_by_age[0], pensionistas_sorted_by_age[-1]

    def sumaPromedio(self):
        total_promedio_gastos = sum(sum(p.gastos_mensuales) / len(p.gastos_mensuales) for p in self.pensionistas)
        return total_promedio_gastos

    def mediaMaxima(self):
        max_avg = 0
        max_avg_name = ""
        max_avg_id = ""

        for pensionista in self.pensionistas:
            avg_gastos = sum(pensionista.gastos_mensuales) / len(pensionista.gastos_mensuales)
            if avg_gastos > max_avg:
                max_avg = avg_gastos
                max_avg_name = pensionista.nombre
                max_avg_id = pensionista.identificador

        return max_avg, max_avg_name, max_avg_id

    def gastoPromedio(self, lst):
        gasto_promedio_list = []
        for pensionista in self.pensionistas:
            avg_gastos = sum(pensionista.gastos_mensuales) / len(pensionista.gastos_mensuales)
            gasto_promedio_list.append(avg_gastos)

        return sorted(gasto_promedio_list)








