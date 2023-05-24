def es_par(numero):
    """
    Esta función verifica si un número es par o impar.

    >>> es_par(2)
    True
    >>> es_par(3)
    False
    >>> es_par(0)
    True
    >>> es_par(-2)
    True
    >>> es_par(-3)
    False
    """
    if numero % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)