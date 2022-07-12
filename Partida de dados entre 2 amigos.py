
'''
es este ercicio:
https://parzibyte.me/blog/2022/05/28/python-partida-dados-entre-2-amigos-ejercicio-resuelto/

Crea un programa que simule una partida de dados entre dos amigos, siendo las normas del juego las siguientes:
-Cada jugador lanzará dos dados de 6 simultáneamente y apuntará los resultados que han obtenido.
-Si alguno de los números obtenidos por los jugadores coincide, el Jugador 1 ganará la ronda. Por el contrario, si ninguno de los números coincide el Jugador 2 ganará.
-El juego finalizará cuando alguno de los jugadores gane 3 rondas.
-El programa deberá enviar un mensaje de enhorabuena al jugador que haya ganado la partida y terminarse.
'''

from random import randrange


def tirar_dados():
    resultado = randrange(1, 6)
    #print(f'-Tirando el dado: Ha salido el {resultado}')
    return resultado


jugador1_puntuacion = 0
jugador2_puntuacion = 0


jugador1 = input('¿Cuál es el nombre del primer jugador? ')
jugador2 = input('¿ y cuál es el nombre del segundo jugador? ')

for x in range(1,4):
    jugador1_dado1 = tirar_dados()
    jugador1_dado2 = tirar_dados()

    print(f'-{jugador1} tira sus dados y ha obtenido este resultado: {jugador1_dado1} y {jugador1_dado2}')

    jugador2_dado1 = tirar_dados()
    jugador2_dado2 = tirar_dados()

    print(f'-{jugador2} tira sus dados y ha obtenido este resultado: {jugador2_dado1} y {jugador2_dado2}')


    if jugador1_dado1 in [jugador2_dado1, jugador2_dado2] or jugador1_dado2 in [jugador2_dado1, jugador2_dado2]:
        print(f'En la ronda {x} el jugador 1, {jugador1} ha ganado porque han coincidido')
        jugador1_puntuacion =+1
    else:
        print(
            f'En la ronda {x} el jugador 2, {jugador2} ha ganado porque no coinciden las tiradas')
        jugador2_puntuacion = +1

print()
if jugador1_puntuacion < jugador2_puntuacion:
    print(f'Gano el jugador 1: {jugador1}')
else:
    print(f'Gano el jugador 2: {jugador2}')
