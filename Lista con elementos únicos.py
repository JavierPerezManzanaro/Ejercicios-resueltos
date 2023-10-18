numeros = [1, 2, 2, 3, 3, 4, 5]


def obten_numeros_unicos(numeros):
    lista_de_numeros_unicos = []
    numeros_unicos = set(numeros)
    for numero in numeros_unicos:
        lista_de_numeros_unicos.append(numero)
    return lista_de_numeros_unicos


def obten_numeros_unicos_por_iteracion(numeros):
    unicos = []
    for numero in numeros:
        if numero in unicos:
            continue
        else:
            unicos.append(numero)
    return unicos


def obten_numeros_unicos_por_iteracion_if_negativo(numeros):
    unicos = []
    for numero in numeros:
        if numero not in unicos:
            unicos.append(numero)
    return unicos

""" Otras formas:
- Utilizar métodos de lista incorporados 
    .count() y .remove() para eliminar elementos duplicados
- Utilice los elementos de la lista como claves del diccionario para eliminar duplicados
"""


print('Usar un SET y pasar al final lista')
print(obten_numeros_unicos(numeros))
print(type(obten_numeros_unicos(numeros)))

print('Usar un SET y pasar al final lista, con menos código')
numeros_unicos = list(set(numeros))
print(numeros_unicos)
print(type(numeros_unicos))

print('Una iteración para localizar a los valores únicos')
print(obten_numeros_unicos_por_iteracion(numeros))
print(type(obten_numeros_unicos_por_iteracion(numeros)))


print('Una iteración para localizar a los valores únicos con un if en negativo')
print(obten_numeros_unicos_por_iteracion(numeros))
print(type(obten_numeros_unicos_por_iteracion(numeros)))
