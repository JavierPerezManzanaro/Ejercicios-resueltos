def invertir_cadena(cadena):
    longuitud = len(cadena)
    for indice in range(longuitud):
        #print(indice)
        print(cadena[longuitud-indice-1: longuitud-indice: 1], end='')
    print()

if __name__ == '__main__':
    invertir_cadena('esta es la cadena a invertir')
    invertir_cadena('ritrevni a anedac al se atse')
