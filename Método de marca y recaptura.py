"""
He aquí la trampa. Se trata de reemplazar el problema original por otro más simple, y luego volver al problema de interés, otro viejo truco de la matemática.

Nuestro problema es estimar el total de tortugas. Estoy muy tentado de llamar “N” a esta cifra apelando a la práctica habitual algebraica, que sugiere reemplazar magnitudes desconocidas por letras. Pero como le prometí al editor que no iba a usar jerga ni símbolos, llamaré a esta magnitud desconocida “Marcela”, en honor a una colega matemática.

Bien, cuando subimos al bote por primera vez, pintamos 20 tortugas, o sea que en toda la laguna la proporción de tortugas pintadas es 20 dividido Marcela. Si Marcela fuese 200, quiere decir que fueron pintadas el 10% de las tortugas.

Aquí viene la trampa. Ya devolvimos las tortuguitas a la laguna y supongamos que ahora el problema no es contar la cantidad de tortugas (cuánto da Marcela), sino ver si podemos estimar la proporción de tortugas pintadas. Volvemos al bote, capturamos 40 tortugas y observamos que 5 tenían la marca. Es decir, 5 dividido 40 me tiene que dar la proporción de tortugas pintadas en la muestra de tortugas recapturadas. Da 12,5%.
Ahora volvamos a la primaria. 5 es a 40 lo que 20 a Marcela. Es decir, 5 sobre 40 (proporción de tortugas recapturadas con la marca blanca) es una estimación de la proporción de tortugas pintadas (proporción de tortugas marcadas, dividido Marcela, el total de tortugas). Un simple uso de la regla de tres simple dice que Marcela debería ser 160, de modo que 20 sobre Marcela (160) da lo mismo que 5 sobre 40. Je, je.


La cantidad total de porotos estimada es: la cantidad de porotos que pintamos de negro inicialmente, multiplicada por la cantidad de porotos que sacamos en la segunda vez, todo dividido por la cantidad de porotos con marca que salieron la segunda vez.

"""


if __name__ == '__main__':
    print('¿Cuantas tortugas hay en un estanque?')
    print()
    print()

    elementos_marcados = int(input('Sales en barca y ¿Cuantas tortugas marcas? '))
    print()
    elementos_segunda_tanda = 0
    elementos_segunda_marcadas = 0
    paso = False
    while paso==False:
        elementos_segunda_tanda = int(input('Sales la segunda vez y ¿Cuantas tortugas capturas? '))
        elementos_segunda_marcadas = int(input('De las cuales: ¿Cuantas tortugas estan marcadas? '))
        if elementos_segunda_marcadas < elementos_segunda_tanda:
            paso = True
        else:
            print('Las tortugas marcadas no pueden ser mas que las que has recogido')
            paso = False

    #* Lógica de la app:
    print()
    print('El proceso es simple: el problema se divide en dos mas pequeños: 1) por una parte vamos a ver el porcentaje de tortugas pintadas en el segundo paseo. Ahora ese porcentaje ')
    poblacion_calculada = ((elementos_marcados * elementos_segunda_tanda)/ elementos_segunda_marcadas)
    print()
    print(f'La población de tortugas es de {poblacion_calculada} ejemplares.')
