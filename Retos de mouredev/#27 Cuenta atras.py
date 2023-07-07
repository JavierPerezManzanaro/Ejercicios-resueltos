"""
/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */
"""

import time

def cuenta_atras(duracion: int, paso:int):
    time.sleep(paso*duracion)



if __name__ == '__main__':
    duracion = int(input('¿Cuantos pasos quieres esperar? '))
    paso = int(input('¿Cuanto dura cada paso? '))

    inicio = time.time()
    cuenta_atras(duracion, paso)
    fin = time.time()
    print(f'La función ha durado: {fin-inicio} segundos')
