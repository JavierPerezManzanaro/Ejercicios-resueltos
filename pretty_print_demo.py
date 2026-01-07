import pprint

# Clase de ejemplo para ilustrar el uso de pprint
class Estudiante:
    def __init__(self, nombre, edad, cursos):
        self.nombre = nombre
        self.edad = edad
        self.cursos = cursos

    def __repr__(self):
        return f'Estudiante(nombre={self.nombre}, edad={self.edad}, cursos={self.cursos})'


if __name__ == "__main__":

    # Creando una lista de estudiantes
    estudiantes = [
        Estudiante('Alice', 23, ['Matemáticas', 'Física']),
        Estudiante('Bob', 21, ['Literatura', 'Historia']),
        Estudiante('Charlie', 22, ['Biología', 'Química'])
    ]

    # Creando un diccionario de estudiantes con sus calificaciones
    calificaciones = {
        'Alice': {'Matemáticas': 95, 'Física': 89},
        'Bob': {'Literatura': 82, 'Historia': 75},
        'Charlie': {'Biología': 88, 'Química': 90}
    }

    # Usando PrettyPrinter para imprimir la lista de estudiantes
    pp = pprint.PrettyPrinter(indent=4)
    print('Lista de Estudiantes:')
    pp.pprint(estudiantes)

    # Usando PrettyPrinter para imprimir el diccionario de calificaciones
    print('\nCalificaciones de los Estudiantes:')
    pp.pprint(calificaciones)

    # Imprimir una representación en cadena del diccionario
    calificaciones_str = pp.pformat(calificaciones)
    print('\nRepresentación en cadena de las Calificaciones:')
    print(calificaciones_str)
