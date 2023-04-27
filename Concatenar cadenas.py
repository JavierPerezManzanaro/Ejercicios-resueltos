# Concatenar cadenas con .join()


lista_de_cadenas = ["Hello", "my", "friend"]

# normal
mi_cadena = ""
for i in lista_de_cadenas:
    mi_cadena += i + " "
print (mi_cadena)

# mejor manera
mi_cadena = " ".join(lista_de_cadenas)
print (mi_cadena)