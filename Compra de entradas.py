'''
Supón que estás diseñando una aplicación que permite cobrar el precio de entrada a un evento deportivo. Las tarifas establecidas, en función de la edad, son:

Las personas menores de 6 años no pagan entrada.
Las personas menores entre 6 y 18 años pagan una tarifa reducida de 10 €.
Las personas mayores de edad pagan 20 €.5
Genera un código en Python que pregunte la edad de la persona a la que se va a comprar la entrada y que devuelva por pantalla cuánto le costará dicha entrada.

(Advertencia: comprueba si los datos que capta el sistema corresponden a caracteres o a valores numéricos; en el primer caso tendrás que transformar dicho dato en una variable numérica, por ejemplo, mediante la función int()).



'''

print('Comprar entradas')
print('----------------')
print('0 para salir')
print('versión 3')
edad = None
while edad != 0:
    try:
        edad = int(input('¿Edad del visitante? '))
    except:
        print('Mete un valor numérico')
    else:
        if edad == 0:
            print('Salir')
        elif edad <= 5:
            print('Es menor de 6 años: Pasa gratis')
        elif edad >= 6 and edad <= 18:
            print('Entre 6 y 18: Cobrar 10€')
        elif edad >= 19:
            print('Más de 18: Cobrar 20€')