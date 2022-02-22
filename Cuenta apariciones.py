'''
Ejercicio #7: Cuenta apariciones
Categoría: Ejercicios
En este ejercicio continuamos repasando los tipos colección de Python. En esta ocasión debes hacer uso de diccionarios.

Requisitos
Escribe un programa que, dada una cadena de texto que se introduce por consola, 
cuente y muestre el número de apariciones de cada carácter en la cadena. Como te decía, 
debes usar el tipo dict para almacenar los resultados.

'''
# https://j2logo.com/ejercicios/ejercicio-7-cuenta-apariciones/



import os
os.system('clear')

print('-'*20)
cadena = str(input('Introduce la cadena: '))
apariciones = {}


for caracter in cadena:
    #print(f'{caracter=}')
    if caracter in apariciones.keys():
        apariciones[caracter] += 1
    else:
        apariciones[caracter] = 1


print(f'{apariciones=}')
print(f'Letras diferentes: {len(apariciones)}')

print(f'Longuitud de la cadena: {len(cadena)}')
print(f'Longuitud de control: {(sum(apariciones.values()))}')


# solución del profesor
caracteres = {}
cadena = input('Introduce una cadena > ')

for c in cadena:
    caracteres[c] = caracteres.get(c, 0) + 1

print('\n'.join([f'{k}: {v}' for k, v in caracteres.items()]))
