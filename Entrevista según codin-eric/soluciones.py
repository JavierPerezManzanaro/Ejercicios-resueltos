"""
1. Definir una función max() que tome como argumento dos numeros y
devuelva el mayor de ellos.
(Es cierto que python tiene una función max() incorporada,
pero hacerla nosotros mismos es un muy buen ejercicio.
"""


from calendar import c
from curses import curs_set


def custom_max(n1: int, n2: int) -> int:
    """Dado dos numeros de entrada retorna el maximo de ambos

    Args:
        n1 (int): Primer numero a comparar
        n2 (int): Segundo numero a comparar

    Returns:
        int : Mayor de ambos
    """
    if n2 > n1:
        return n2
    elif n1 > n2:
        return n1
    elif n1 == n2:
        raise Exception("Los valores no pueden ser iguales")
    raise Exception("Algo salio mal")

"""
1. Definir una función max_de_tres(), que tome tres números como argumentos 
y devuelva el mayor de ellos.
"""

def max_de_tres(n1: int,n2: int,n3: int):
    """Toma tres números como argumentos y devuelva el mayor de ellos.

    Args:
        n1 (int): Primer numero a comparar
        n2 (int): Segundo numero a comparar
        n3 (int): Tercer numero a comparar

    Returns:
        int: Mayor de los tres numeros
    """
    """
    a > b > c
    b > c
    a > c
    """

    n = custom_max(n1, n2)
    n_final = custom_max(n3, n)

    return n_final