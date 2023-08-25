"""
Marcelo Huallpara Rodriguez Grupo 952 16 de Agosto de 2023
Encriptar. Diseñe una función encripta(s, clave), que reciba un string s con un
mensaje y un string con una clave de codificación, y retorne el mensaje codificado
según la clave leída. Los signos de puntuación y dígitos que aparecen en el mensaje
deben conservarse sin cambios.
La clave consiste en una sucesión de las 26 letras minúsculas del alfabeto, las cuales
se hacen corresponder con el alfabeto básico (a...z, sin la ñ o vocales acentuadas) de
26 letras. La primera letra de la clave se relaciona con la letra 'a', la segunda con la
letra 'b', etc. Por ejemplo, una entrada de la forma:
Clave = 'ixmrklstnuzbowfaqejdcpvhyg'
Texto para codificar: 'cafe'
Con esta clave la letra 'i' se corresponde con la letra 'a', la letra 'x' se corresponde
con la letra 'b', la letra 'm' se corresponde con la letra 'c', y así sucesivamente, por
lo que el ejemplo anterior debería dar como salida: 'milk'.

Nota: para simplificar consideraremos solo mensajes de entrada en minúsculas.
Ejemplos:
encripta('cafe', ' ixmrklstnuzbowfaqejdcpvhyg')
'milk'
encripta('dame 1 chocolate', ' ixmrklstnuzbowfaqejdcpvhyg')
'riok 1 mtfmfbidk'
bxrbklitjuzbowfrqpjdcpvgug
"""

def encripta(s, clave):
    alfabetobasic = 'abcdefghijklmnopqrstuvwxyz'
    alfabetoclave = clave.lower()
    mensajecodificado = ''

    for char in s:
        if char.isalpha():
            indice = alfabetobasic.index(char)
            char_codificado = alfabetoclave[indice]
            mensajecodificado += char_codificado
        else:
            mensajecodificado += char

    return mensajecodificado

text1 = 'fresa'
key1 = 'ivmrwlstndzbowpacejdcpvhda'
result1 = encripta(text1, key1)
print(result1)

text2 = 'baloncesto'
key2 = 'bxrbklitjuzbowfrqpjdcpvgug'
result2 = encripta(text2, key2)
print(result2)


