'''
Las tuplas son inmutables.
Estas funciones las pasan a lista, las modifican y las devuelven en formato tuple.
'''


def ordenar_tupla(tupla):
  lista=list()
  for i in tupla:
    lista.append(i)
  lista.sort()
  tupla = tuple(lista)
  return tupla


def anadir_elemento(tupla, elemento):
  lista = list(tupla)
  print('Agregado: ', elemento)
  lista.append(elemento)
  tupla = tuple(lista)
  return tupla


def eliminar_elemento(tupla, elemento):
  nueva=list()
  print ('Elemento a eliminar: ',elemento)
  for c in list(tupla):
    if not c == elemento:
      nueva.append(c)
  return tuple(nueva)

t=tuple()
t=('4','9','3','0','2')
print ('original:',t)
print ('ordenada:', ordenar_tupla(t))
print (anadir_elemento(t,'5'))
print (eliminar_elemento(t,'9'))