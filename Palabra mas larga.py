# -*- coding: utf-8 -*-


'''
Escribir una función mas_larga()
que tome una lista de palabras
y devuelva la mas larga.
'''

# https://github.com/scsjonatan/Ejercicios-Python/blob/master/palabra_mas_larga.py


def mas_larga(cadena):
    palabras = cadena.split()
    extension = 0
    lista_de_palabras = set(palabras)
    diccionario = {}
    for palabra in lista_de_palabras:
        extension = len(palabra)
        diccionario[palabra]= extension
    resultado = max(diccionario.items(), key=lambda x: x[1])[0]
    #print(f'{diccionario=}')
    print(f'{resultado=}')


def mas_larga_2(cadena):
    lista = cadena.split()
    longuitud_palabra_mayor = 0
    for palabra in lista:
        if len(palabra) >= longuitud_palabra_mayor:
            longuitud_palabra_mayor = len(palabra)
            palabra_mayor = palabra
    print(f'{palabra_mayor=}')



cadena = '''
Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo,
fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo.
Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi.
Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim.
Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum.
Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui.
Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,
          '''

mas_larga(cadena)
print()
mas_larga_2(cadena)