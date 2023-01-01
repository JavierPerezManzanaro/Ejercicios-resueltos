import shelve

shelf = shelve.open('Presistencia de datos/datos')
shelf['nombre'] = 'Javier'
shelf['ciudad'] = 'Madrid'
shelf['edad'] = '22'
shelf.close()