''''
ejercico 1 de:
https://www.udemy.com/course/curso-resolver-ejercicios-reales-de-entrevistas-tecnicas-programador/learn/lecture/27096546#overview
'''


def con_slicing(word):
    if str(word) == str(word[::-1]):
        print('Método 1: Es palindromo')
    else:
        print('Método 1: No es palindromo')


def con_condicion(word):
    inicio = 0
    fin = len(word) - 1
    while word[inicio] == word[fin]:
        if inicio >= fin:
            return True
        inicio += 1
        fin -= 1
    return False


def con_condicion_recursivo(word, inicio, fin):
    if inicio >= fin:
        return True
    if word[inicio] == word[fin]:
        return con_condicion_recursivo(word, inicio+1, fin-1)
    else:
        return False


if __name__ == '__main__':
    word = input('¿Escribe la palabra analizar? ')

    con_slicing(word)
    print('Método 2: '+str(con_condicion(word)))
    print('Método 3: '+str(con_condicion_recursivo(word, 0, len(word)-1)))
