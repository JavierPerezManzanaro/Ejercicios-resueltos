"""
5
Definir una función inversa() que calcule la inversión de una cadena.
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"


Información sacada de: https://www.delftstack.com/es/howto/python/python-iterate-list-backwards/

"""

# método 1: range
def inversa1(cadena):
    cadena_nueva = ''
    for posicion in range(len(cadena)-1,-1,-1):
        cadena_nueva = cadena_nueva + cadena[posicion]
    return cadena_nueva


# método 2: reversed()
def inversa2(cadena):
    cadena_nueva = ''
    for i in reversed(cadena):
        cadena_nueva = cadena_nueva + i
    return cadena_nueva


# metodo 3: for
def inversa3(cadena):
    cadena_nueva = ''
    for i in cadena[::-1]:
        cadena_nueva = cadena_nueva + i
    return cadena_nueva


print(inversa1("estoy probando"))
print(inversa2("estoy probando"))
print(inversa3("estoy probando"))
