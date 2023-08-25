"""
Marcelo Huallpara Rodriguez Grupo 952 16 de Agosto de 2023
Desencriptar. Diseña una función desencripta(s, clave) que realice la función inversa
a la función anterior, es decir, reciba un string s y una clave y realice la desencriptación
del mensaje en el string devolviendo la cadena desencriptada. Ejemplos:

clave = ' ixmrklstnuzbowfaqejdcpvhyg'

desencripta('milk',clave)
'cafe'

desencripta('riok 1 mtfmfbidk',clave)
'dame 1 chocolate'
"""

def desencripta(s, clave):
    genera_clave = {clave[i]: chr(97 + i) for i in range(len(clave))}
    desencriptado = []

    for char in s:
        if char in genera_clave:
            desencriptado.append(genera_clave[char])
        else:
            desencriptado.append(char)
    return ''.join(desencriptado)

clave1 = 'ivmrwlstndzbowpacejdcpvhda'
clave2 = 'bxrbklitjuzbowfrqpjdcpvgug'
print(desencripta('lewji', clave1))
print(desencripta('xbbfwrkjdf', clave2))
