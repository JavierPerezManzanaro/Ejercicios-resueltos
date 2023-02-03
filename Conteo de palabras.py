texto = input('Cadena para contar las palabras: ')
repeticiones = dict()
palabras = texto.lower().replace(",","").replace(".","").split()
for palabra in palabras:
    if palabra not in repeticiones:
        repeticiones[palabra]=1
    else:
        repeticiones[palabra] += 1
print(repeticiones)
