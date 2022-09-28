#!/usr/bin/env python3


'''
Vamos a analizar una cadena en la que los ( [ y { se cierren en orden
( = 40
) = 41
  = 32
[ = 91
] = 93
  = 32
{ = 123
} = 125
'''


def mostrarASCII():
    string = '''() [] {}'''
    for ch in string:
        print(ch + ' = ' + str(ord(ch)))

def cadena_correcta(cadena) -> bool:
    estado = True
    if '(' in cadena and ')' not in cadena:
        print('Con ( pero sin )')
        estado = False
    if '[' in cadena and ']' not in cadena:
        print('Con [ pero sin ]')
        estado = False
    if '{' in cadena and '}' not in cadena:
        print('Con { pero sin }')
        estado = False
    if estado == True:
        if cadena.find(chr(40)) > cadena.find(chr(41)):
            print(f'{cadena.find(chr(40))} > {cadena.find(chr(41))}')
            print('() mal cerrado')
            estado = False
        if cadena.find('[') > cadena.find(']'):
            print(f"{cadena.find('[')} > {cadena.find(']')}")
            print('[] mal cerrado')
            estado = False
        if cadena.find('{') > cadena.find('}'):
            print('{} mal cerrado')
            estado = False
    return estado

if __name__ == '__main__':
    #mostrarASCII()
    cadena = input('Introduce la cadena a analizar: ')
    print(f'La cadena es: {cadena_correcta(cadena)}')
