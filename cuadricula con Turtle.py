from turtle import *
import os

# https://www.mclibre.org/consultar/python/lecciones/python-turtle-1.html
# https://docs.python.org/es/3.10/library/turtle.html
# https://victomanolo.wordpress.com/turtle/

#! CUIDADO
#todo por hacer
#? aviso
#* explicación

'''Se lo dedico a Izan, que se que le gusta
'''

def pintar(x, y, tono):
    penup()
    goto((espacio_entre_columnas*(x-1)), (espacio_entre_filas*(y-1)))
    pendown()

    color(GAMA_COLORES[tono])
    begin_fill()
    for _ in range(2):
        forward(espacio_entre_filas)
        right(90)
        forward(espacio_entre_columnas)
        right(90)
    end_fill()
    return




os.system('clear')


#* descomentar esto
# ancho = int(input('Ancho: '))
# alto = int(input('Alto: '))
# columnas = int(input('Número de columnas: '))
# filas = int(input('Número de filas: '))
ancho = 700
alto = 700
columnas = 10
filas = 10

GAMA_COLORES = {
    1: 'cyan',
    2: 'red',
    3: '#285078',
    4: '#666666',
}

broma = ((4, 1, 4), (7, 1, 4), 
         (3, 2, 4), (4, 2, 4), (5, 2, 4), (6, 2, 4), (7 ,8, 4),
         (2 ,3 ,4), (3, 3, 4), (4, 3, 4), (5, 3, 4), (6, 3 , 4), (7, 3, 4), (8, 3, 4), (9, 3, 4),
         (2, 4, 4), (3, 4, 4), (4, 4, 4), (5, 4,
                                           4), (6, 4, 4), (7, 4, 4), (8, 4, 4),
         (2, 5, 4), (3, 5, 4), (4, 5, 4), (5, 5, 4), (6, 5, 4), (7, 5, 4), 
         (2, 6, 4), (3, 6, 4), (4, 6, 4), (5, 6, 4), (6, 6, 4), (7, 6, 4), 

         )

espacio_entre_filas = int(alto/filas)
espacio_entre_columnas = int(ancho/columnas)

setup(ancho, alto, 0, 0)
title('Cuadricula')

reset()

setworldcoordinates(0, 0, ancho, alto)
hideturtle()
speed(10)

#* dibujamos cuadricula
fd(ancho)
for x in range(filas):
    penup()
    goto(0, espacio_entre_filas*(x+1))
    pendown()
    fd(ancho)
penup()
goto(0 ,0)
right(-90)
pendown()
fd(alto)
for x in range(columnas):
    penup()
    goto(espacio_entre_columnas*(x+1), 0)
    pendown()
    fd(alto)

print('Abajo a la izquierda es 1, 1')
print('Los colores disponibles son estos:')
for key in GAMA_COLORES:
    print(key, '=', GAMA_COLORES[key])

x = 1
while x != int:
    print()
    print('Escribe los valores separados por espacios')

    datos = input('Columna X | Fila Y | color: ')
    x, y, tono = datos.split(' ')
    if x == 'broma':
        for valores in broma:
            x, y, tono = valores
            pintar(x, y, tono)
        break
    x = int(x)
    y = int(y)
    tono = int(tono)

    pintar(x, y , tono)



    
done()
