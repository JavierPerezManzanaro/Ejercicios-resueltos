import collections

# Crear un nuevo tipo de tupla para contener datos
# de elementos químicos

elemento = collections.namedtuple('elemento',
                                  ['nombre', 'simbolo', 'numato'])

# Crear un nuevo objeto del tipo elemento,
# con datos del Azufre

elem = elemento('Azufre', 'S', 16)

# Mostrar información del objeto anterior

print(elem.nombre, elem.simbolo, elem.numato)  # Azufre S 16
print(elem[0], elem[1], elem[2])  # Azufre S 16
print(elem)  # elemento(nombre='Azufre', simbolo='S', numato=16)

# Conocer de qué tipo es el objeto 'elem'

print(type(elem))  #

# Mostrar la definición de la subclase 'elem'

#print(elem._source)

# Mostrar los nombres de campos de la subclase 'elem'

print(elem._fields)
# nombres de campos: ('nombre', 'simbolo', 'numato')

# Sustituir los valores actuales

elem = elem._replace(nombre='Carbono', simbolo='C', numato=6)

# Mostrar información

print(elem.nombre)  # 'Carbono'

# Mostrar tipo de diccionario con los campos ordenados
# como en una tupla

print(elem._asdict())

# Obtener el valor del campo indicado

print(getattr(elem, 'simbolo'))  # 'C'
