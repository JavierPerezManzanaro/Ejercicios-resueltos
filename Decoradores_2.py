def log(fichero_log):
    def decorador_log(func):
        def decorador_funcion(*args, **kwargs):
            with open(fichero_log, 'a') as opened_file:
                output = func(*args, **kwargs)
                opened_file.write(f"{output}\n")
        return decorador_funcion
    return decorador_log

@log('Decoradores_2_suma.log')
def suma(a, b):
    return a + b

@log('Decoradores_2_resta.log')
def resta(a, b):
    return a - b

@log('Decoradores_2_multiplicación.log')
def multiplicadivide(a, b, c):
    return a*b/c



suma(10, 30)
resta(7, 23)
multiplicadivide(5, 10, 2)