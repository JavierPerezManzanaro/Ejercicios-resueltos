def my_first_generator():
    print('Paso 1')
    yield 1
    print('Paso 2')
    yield 2
    print('Paso 3')
    yield 3


def foo(secuencia):
    print('Empieza la ejecución del código...')
    for item in secuencia:
        yield item
        print(item)


gen = my_first_generator()
print(next(gen))
print(next(gen))



ejemplo2 = foo('abcd')
print(type(ejemplo2))
ejemplo2.__next__()
ejemplo2.__next__()
ejemplo2.__next__()
