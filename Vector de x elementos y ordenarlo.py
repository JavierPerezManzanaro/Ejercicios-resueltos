# ejerccio 5.8 de PB_Practicas_Python.pdf


import random


numero_de_elementos = int(input('¿Número de elementos? '))
valor_max = int(input('¿Valor máximo? '))
valor_min = int(input('¿Valor mínimo? '))
vector = []

for posicion in range(numero_de_elementos):
    valor = random.randint(valor_min, valor_max)
    vector.append(valor)
    print(f'La posción {posicion} vale {valor}')

print()
print('Lista original:')
print(f'{vector=}')

print()
print('Lista ordenada:')
vector = sorted(vector)
print(f'{vector=}')
