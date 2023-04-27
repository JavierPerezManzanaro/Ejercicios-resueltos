# Ordenar iterables complejos
data = [
    {"nombre": "Javier", "edad": 52},
    {"nombre": "Izan", "edad": 18},
    {"nombre": "Andre", "edad": 32},
]
data_ordenada = sorted(data, key=lambda x: x["edad"])
print(data_ordenada)