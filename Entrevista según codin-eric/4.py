"""
4
Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""


def sum(lista):
    suma = 0
    for elemento in lista:
        suma = suma + elemento
    return suma


def multip(lista):
    for posicion in range(1,len(lista)-2):
        #print(f'{multiplicacion=} = {lista[posicion]=} * {lista[posicion]+1=}')
        paso1 = lista[posicion] * lista[posicion+1]
        paso2 = paso1 * lista[posicion+2]
    return paso2


print(sum([1, 2, 3, 4]))
print(multip([1, 2, 3, 4]))
