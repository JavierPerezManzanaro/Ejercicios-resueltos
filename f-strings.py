import math
print('''Docuemntación extraida de principalmente de Documentation on f-strings Updated''')




print('Alineación de textos o variables')
print('--------------------------------')
print(f"|{'Por defeto':25}|")
print(f"|{'Derecha':<25}|")
print(f"|{'Izquierda':>25}|")
print(f"|{'Centrado':^25}|")
print()
variable = math.pi
print(f"Con números {variable = }")
print(f"|{variable:25}|")
print(f"|{variable:<25}|")
print(f"|{variable:>25}|")
print(f"|{variable:^25}|\n")
variable = "Python 3.10.4"
print(f"Con textos {variable = }")
print(f"|{variable:25}|")
print(f"|{variable:<25}|")
print(f"|{variable:>25}|")
print(f"|{variable:^25}|")

print('Alineación de textos o variables y relleno')
print('------------------------------------------')
print('Cadena:[caracter de relleno][< > ó ^][]')
print(f"|{'Derecha':_<25}|") 
print(f"|{'Izquierda':_>25}|") 
print(f"|{'Centrado':_^25}|")


import locale
number = 9876543.21
formatted_number = f"Número formateado antes: {number:n}"
print(formatted_number)
# Configurar el locale para España (es-ES)
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

number = 9876543.21
print(f"Número formateado :n -> {number:n}")
print(f"Número formateado :f -> {number:f}")