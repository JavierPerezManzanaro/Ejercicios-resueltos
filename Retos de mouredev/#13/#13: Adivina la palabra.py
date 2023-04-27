#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2313%20-%20ADIVINA%20LA%20PALABRA%20%5BMedia%5D/ejercicio.md


# ! CUIDADO
# todo por hacer
# ? aviso
# * explicación

"""/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */
 """

import random
import os


def palabra_con_huecos(palabra_seleccionada_modificada, dificultad, longitud):
    vuelta = 0
    while vuelta < dificultad:
        caracter = random.randint(0, longitud-1)
        if palabra_seleccionada_modificada[caracter] != '_':
            palabra_seleccionada_modificada = palabra_seleccionada_modificada.replace(palabra_seleccionada_modificada[caracter],'_',1)
            vuelta += 1
        else:
            pass
    #print(f'{palabra_seleccionada_modificada=}')
    return palabra_seleccionada_modificada


if __name__ == '__main__':
    os.system('clear')

    PALABRAS = ['comenzadas', 'comenzados', 'comenzando', 'conduzcáis', 'confianzas', 'contrahizo', 'convenzáis', 'crucifijos', 'danzábamos', 'decrezamos', 'descabezan', 'descabezar', 'descabezas', 'descalzaba', 'desconozca', 'desconozco', 'desmerezca', 'desmerezco', 'desplazaba', 'desplazcan', 'desplazcas', 'disfrazada', 'disfrazado', 'embarazada', 'embarazado', 'embriaguez', 'empalizada', 'emplazadas', 'emplazados', 'emplazando', 'encabezada', 'encabezado', 'enfadadizo', 'enfermizas', 'enfermizos', 'enfurezcan', 'enfurezcas', 'enmudezcan', 'enmudezcas', 'envilezcan', 'envilezcas', 'esforzaban', 'esforzabas', 'esforzamos', 'excavabais', 'excavación', 'excluyamos', 'exhibición', 'exhibíamos', 'exhumabais', 'exhumación', 'extrajeran', 'extrajeras', 'extrajeron', 'extrajesen', 'extrajeses', 'extrajiste', 'extranjera', 'extranjero', 'fallezcáis', 'finalizaba', 'florezcáis', 'forjábamos', 'formalizan', 'formalizar', 'formalizas', 'fortalezca', 'fortalezco', 'forzaremos', 'forzáramos', 'forzásemos', 'herbazales', 'hojeábamos', 'humanizara', 'humanizará', 'humanizaré', 'humanizase', 'humanizáis', 'induzcamos', 'ingravidez', 'inmoviliza', 'inmovilizo', 'inmovilizó', 'izquierdas', 'izquierdos', 'justifique', 'justifiqué', 'lloviznaba', 'mecanizada', 'mecanizado', 'movilizara', 'movilizará', 'movilizaré', 'movilizase', 'movilizáis', 'obedezcáis', 'olvidadiza', 'olvidadizo', 'palidezcan', 'palidezcas', 'pellizcada', 'pellizcado', 'perjudique', 'perjudiqué', 'prefijaban', 'prefijabas', 'prefijamos', 'prefijemos', 'produzcáis', 'pulverizan', 'pulverizar', 'pulverizas', 'rechazaran', 'rechazaras', 'rechazaron', 'rechazarán', 'rechazarás', 'rechazaría', 'rechazasen', 'rechazases', 'rechazaste', 'recrudezca', 'recrudezco', 'reduzcamos', 'reforzaban', 'reforzabas', 'reforzamos', 'reproduzca', 'reproduzco', 'rivalizaba', 'seduzcamos', 'suavizaban', 'suavizabas', 'suavizamos', 'vaporizara', 'vaporizará',
                'vaporizaré', 'vaporizase', 'vaporizáis', 'velozmente', 'viajábamos', 'viboreznas', 'viboreznos', 'vigorizada', 'vigorizado', 'vocalizara', 'vocalizará', 'vocalizaré', 'vocalizase', 'vocalizáis', 'vulcanizan', 'vulcanizar', 'vulcanizas', 'zaheríamos', 'zahieramos', 'zambullida', 'zambullido', 'zumbadoras', 'zumbadores', 'abalanzoba', 'abanicazos', 'abastezcan', 'abastezcas', 'abonanzaba', 'aborrezcan', 'aborrezcas', 'abrazabais', 'acompañara', 'acompañará', 'acompañaré', 'acompañase', 'acompañáis', 'acompañéis', 'acontezcan', 'acontezcas', 'acuñábamos', 'adelgazaba', 'adjudicaba', 'adjudiquen', 'adjudiques', 'afianzadas', 'afianzados', 'afianzando', 'agradezcan', 'agradezcas', 'alborozaba', 'alcanzaban', 'alcanzabas', 'alcanzamos', 'almorzaban', 'almorzabas', 'almorzamos', 'amenazaban', 'amenazabas', 'amenazamos', 'amenazemos', 'amortizaba', 'aparezcáis', 'apetezcáis', 'aplazabais', 'armonizaba', 'arzopispal', 'arzopispos', 'asperezcas', 'avergonzar', 'avergüenza', 'avergüenzo', 'barnizaban', 'barnizabas', 'barnizamos', 'barzoneaba', 'bautizaban', 'bautizabas', 'bautizamos', 'bazucarais', 'bazucaréis', 'bazucarían', 'bazucarías', 'bazucaseis', 'bermejeaba', 'bizcaríais', 'bizcasteis', 'bostezaban', 'bostezabas', 'bostezamos', 'boxeábamos', 'cabezuelas', 'cabrerizas', 'cabrerizos', 'calzaremos', 'calzáramos', 'calzásemos', 'campañoles', 'canalizaba', 'canonizaba', 'capitaliza', 'capitalizo', 'capitalizó', 'carameliza', 'caramelizo', 'caramelizó', 'caraqueñas', 'caraqueños', 'carbonizan', 'carbonizar', 'carbonizas', 'carpetazos', 'cazaríamos', 'cicatrizan', 'cicatrizar', 'cobertizos', 'cojeábamos', 'colonizaba', 'comenzaran', 'comenzaras', 'comenzaron', 'comenzarán', 'comenzarás', 'comenzaría', 'comenzasen', 'comenzases', 'comenzaste', 'compañeras', 'compañeros', 'complexión', 'compunjáis', 'cotizabais', 'cotizables', 'cotización', 'cruzaremos', 'cruzáramos', 'cruzásemos', 'cuajábamos']
    palabra_seleccionada = PALABRAS[random.randint(0, len(PALABRAS))]
    #palabra_jugador = palabra_seleccionada
    intentos = 4
    psoscion = 0
    #print(f'{palabra_seleccionada=}')
    print()
    longitud = len(palabra_seleccionada)

    while True:
        try:
            dificultad = int(input(f'La palabra tiene {longitud} carácteres. ¿Cuantos carácteres quieres ocultar? '))
        except ValueError:
            print('Tienes que introducir un número.')
            continue #todo
        if dificultad > longitud:
            print('Son demasiados caracteres. Por una cifra menor.')
        else:
            break

    #* palabra_jugador vs palabra_seleccionada
    palabra_jugador = palabra_con_huecos(palabra_seleccionada, dificultad, longitud)

    #* Desarrollo del juego
    while intentos > 0:
        print()
        print(f'Palabra a buscar: {palabra_jugador}')
        print(f'Te quedan {intentos} intentos:')
        #* Preguntamos por la letra
        letra = input('-¿Qué letra quieres poner (o la palabra si ya la sabes)? ')
        if letra == palabra_seleccionada:
            print('GANASTE!!!!')
            break
        #* Preguntamos por la posición
        paso_posicion = True
        while paso_posicion:
            try:
                posicion = int(input('-¿Donde la quieres colocar? '))-1 #para adaptar la cadena al usuario que no sabe que empieza por 0
            except ValueError:
                print('Tienes que introducir un número.')
            finally:
                paso_posicion = False
                if posicion > longitud:
                    print(f'La palabra no tiene tantos caracteres. El número máximo es {longitud}.')
                    paso_posicion = True
                if posicion < 0:
                    print('No puede ser negativo.')
                    paso_posicion = True
        #print(f'{posicion=} // {palabra_jugador[posicion]=} ver 2')
        #* Vemos si acerto o no
        if palabra_jugador[posicion] == '_':
            if letra == palabra_seleccionada[posicion]:
                print('Muy bien, has acertado una letra.')
                palabra_jugador = palabra_jugador.replace('_', letra, 1)
            else:
                print(f'No, lo siento, la "{letra}" no va en la posición {posicion+1}.')
        else:
            print('En esa posición no hay "_".')
        if palabra_jugador != palabra_seleccionada:
            intentos -= 1
        else:
            print('GANASTE!!!!')
    print('fin')

