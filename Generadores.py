def my_first_generator():
    print('Paso 1')
    yield 1
    print('Paso 2')
    yield 2
    print('Paso 3')
    yield 3


gen = my_first_generator()
print(next(gen))
print(next(gen))
