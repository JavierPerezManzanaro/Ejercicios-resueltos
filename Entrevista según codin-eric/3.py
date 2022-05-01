"""
3
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""


def vocal(caracter):
    return True if caracter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] else False


print(vocal('9'))
print(vocal('A'))
print(vocal('e'))
print(vocal('v'))
