x = 0
y = 0


"""
El código que proporcionaste marca como True hasta el número 256 debido al uso del operador is en la línea if x is y. El operador is se utiliza para verificar si dos objetos son el mismo objeto en la memoria, es decir, si tienen la misma identidad.

En Python, los números enteros pequeños se almacenan en caché para ahorrar memoria. Esto significa que los enteros pequeños, como los números en tu bucle (del 0 al 300), se almacenan como objetos únicos en la memoria y, por lo tanto, su identidad es la misma. Cuando x e y son valores pequeños, el operador is devuelve True, ya que ambos están apuntando al mismo objeto en la memoria.
Sin embargo, a partir del número 257, Python deja de almacenar estos números en caché y comienza a crear objetos separados en la memoria para cada número. Como resultado, la identidad de x e y ya no es la misma a partir de 257, y el operador is devuelve False.

Para verificar la igualdad de valores en lugar de la identidad, debes usar el operador == en lugar de is.
"""
while x <= 300:
    x += 1
    y += 1
    if x is y:
        print(f"{x},{y} -> TRUE")
    else:
        print(f"{x},{y} -> FALSE")


x = 0
y = 0

while x <= 300:
    x += 1
    y += 1
    if x == y:
        print(f"{x},{y} -> TRUE")
    else:
        print(f"{x},{y} -> FALSE")
