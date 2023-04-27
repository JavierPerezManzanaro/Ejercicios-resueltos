from collections import Counter



lista = [1, 1, 11, 111, 1, 1, 2, 4, 5, 3, 5, 5, 5, 5]
counter = Counter(lista)
print(counter)

# mostramos cuantas veces aparece del valor 5
print(counter[5])