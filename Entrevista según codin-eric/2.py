"""
2
Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""


def max_de_tres(valor1, valor2, valor3):
    """Devuelve el mayor de los tres.
    Al no ser pedido no indago sobre el tipo de datos.

    Args:
        valor1 (int): valor 1
        valor2 (int): valor 2
        valor3 (int): valor 3

    Returns:
        int: el mayor

    python3 -m doctest -v Entrevistas/2.py
    >>> max_de_tres(8, 4, 10)
    10
"""

    lista = [valor1, valor2, valor3]
    lista.sort(reverse=True)
    return lista[0]


print(max_de_tres(8, 40, 10))
