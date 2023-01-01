import shelve

shelf = shelve.open('Presistencia de datos/datos')
print(shelf['nombre'])