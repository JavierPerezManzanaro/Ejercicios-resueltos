from collections import deque


def revisar(cadena):
    cola = deque()
    for caracter in cadena:
        if caracter == "(":
            cola.append(caracter) #agrega al cominzo
        elif caracter == ")":
            if len(cola) > 0:
                cola.pop() #elimina del final
            else:
                return False

    if len(cola) != 0:
        return False

    return True



print(revisar('((ewe)())((s4334)'))