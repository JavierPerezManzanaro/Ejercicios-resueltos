def palindromo (sentence):
    """Retorna verdadero si el parámetro es un palíndromo en caso contrario retorna falso
    sentence -- String o entero
    
    >>> palindromo("anita lava la tina")
    True
    >>> palindromo (12321)
    True
    >>> palindromo ("CodigoFacilito")
    False
    """
    sentence = str (sentence).lower().replace(" ", "")
    return sentence == sentence[::-1]


print(palindromo('ana'))

#python3 -m doctest 'Palindromo con DocTest y DocString con doctest.py'