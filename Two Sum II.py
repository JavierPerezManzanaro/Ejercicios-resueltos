"""
Declaración del problema


Dado un array de números enteros y un objetivo de búsqueda entero, devuelve índices de los dos números de manera que se sumen al objetivo.

Otra declaración:

https://rohithv63.medium.com/leetcode-167-two-sum-ii-input-array-is-sorted-17ed90d3a6c1
Dada una matriz de números enteros indexados a 1 que ya está ordenada en orden no decreciente, encuentre dos números de tal manera que se sume a un número objetivo específico. Deje que estos dos números sean números[index1] y números[index2] donde 1 <= index1 < index2 <= numbers.length.

Devuelve los índices de los dos números, index1 e index2, sumados por uno como una matriz entera [index1, index2] de longitud 2.

Las pruebas se generan de tal manera que hay exactamente una solución. No puedes usar el mismo elemento dos veces.

Su solución solo debe usar espacio adicional constante.


"""

"""
Test Cases

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

"""

def twoSunII(lista: list, target: int):
    elementos_seleccionados = []
    par_seleccionado = []
    for elemento1 in lista:
        for elemento2 in lista:
            # print(f'{elemento1=} -- {elemento2=}')
            if elemento1 + elemento2 == target:
                print(f'{elemento1=} -- {elemento2=}: suma correcta')
                par_seleccionado.append(elemento1)
                par_seleccionado.append(elemento2)
                elementos_seleccionados.append(par_seleccionado)
                
    # elementos_seleccionados_unicos = elementos_seleccionados #set(elementos_seleccionados)
    # print(f'{elementos_seleccionados_unicos=}')
    # resultado = []
    # for numero in elementos_seleccionados_unicos:
    #     #resultado = lista.index(numero)+1
    #     resultado.append(lista.index(numero)+1)
    #     # print(f'{resultado=}')

    return elementos_seleccionados



if __name__=='__main__':
    numbers = [2,7,11,15]
    target = 9
    print(twoSunII(numbers, target))

    print()

    numbers = [2,3,4]
    target = 6
    print(twoSunII(numbers, target))