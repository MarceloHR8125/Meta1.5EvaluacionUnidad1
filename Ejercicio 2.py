"""
Marcelo Huallpara Rodriguez Grupo 952 16 de Agosto de 2023
Suma de dos números. Dado una lista de números enteros y un valor entero
(target), retorna el índice de los dos números que sumados sean igual al target.
Debe asumir que existe siempre una única solución, y que los elementos no se pueden
usar dos veces. Debes retornar una tupla con los índices.
Ejemplos:
nums = [2, 7, 11, 15]
target = 9
busquedaSuma(nums, target)
(0, 1)

nums = [3, 2, 4]
target = 6
busquedaSuma(nums, target)
(1, 2)
"""

def busquedaSuma(nums, target):
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return (num_indices[complement], i)
        num_indices[num] = i
    return None
nums1 = [2, 6, 9, 11]
target1 = 8
print(busquedaSuma(nums1, target1))

nums2 = [4, 7, 9, 12]
target2 = 11
print(busquedaSuma(nums2, target2))
