'''
4.13 Crea un programa llamado ex_4_13 que dibuje una rejilla con rectángulos, como la de la figura, 
a partir de un cuatro números enteros introducidos por el usuario que serán 
1) el número de rectángulos por fila, 
2) el número de rectángulos por columna, y 
3) la altura y 
4) la anchura en caracteres del interior del rectángulo. 


Por ejemplo, para 4 rectángulos por fila, 3 rectángulos por columna, un ancho de 5 y un alto de 2, el programa debe imprimir:

'''


columnas = int(input('¿Cuantas columnas? '))
filas = int(input('¿Cuantas filas? '))
ancho = int(input('¿Ancho? '))
alto = int(input('¿Alto? '))
print('')


def linea_horizontal_rellena(columnas, ancho):
    return((('+'+'-'*ancho)*columnas)+'+')


def linea_horizontal_hueca(columnas, ancho):
    return((('|'+' '*ancho)*columnas)+'|')


for linea in range(1, filas+1):
    #print(f'{linea=}')
    if linea == 1:
        print(linea_horizontal_rellena(columnas, ancho))
    for x in range(alto):
        print(linea_horizontal_hueca(columnas, ancho))
    print(linea_horizontal_rellena(columnas, ancho))

print('')

print('Otra forma más fácil con multiplicación de un número por un string:')


tapa = (('+'+'-'*ancho)*columnas)+'+ \n'
caja = (('|'+' '*ancho)*columnas)+'| \n'
tapa_y_caja = (tapa + caja*alto) * filas + tapa
print(tapa_y_caja)