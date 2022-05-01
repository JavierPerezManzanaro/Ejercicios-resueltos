"""
1
Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""


def custom_max(valor1: int, valor2: int) -> int:
    """devuelve el mayor de dos valores, no hace comprovaciones del tipo del valor al no ser pedido

    Args:
        valor1 (int): valor númerico 1
        valor2 (int): valor númerico 2

    Returns:
        int: el mayor de los dos

    python3 -m doctest -v Entrevistas/1.py
    >>> custom_max(8, 15)
    15
    """
    return valor1 if valor1 > valor2 else valor2


print(custom_max(8, 4))
