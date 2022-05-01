"""
6
Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas),
ejemplo: es_palindromo ("radar") tendría que devolver True.
"""


def es_palindromo(palabra):
    longuitud = len(palabra)
    mitad = round(longuitud/2)
    for i in range(0, mitad):
        if palabra[i] == palabra[longuitud-1-i]:
            es = True
        else:
            es = False
            break
    return es


print(es_palindromo("radar"))
