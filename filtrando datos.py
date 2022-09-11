from unicodedata import name


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    desarrolladores_python = [trabajador['name']
                              for trabajador in DATA if trabajador['language'] == 'python']
    print('Desarrolladores de python: ')
    for trabajador in desarrolladores_python:
        print(trabajador)

    trabajadores_platzi = [trabajador['name']
                           for trabajador in DATA if trabajador['organization'] == 'Platzi']
    print()
    print('Trabajadores de Platzi: ')
    for trabajador in trabajadores_platzi:
        print(trabajador)

    mayores_de_18 = list(
        filter(lambda trabajador: trabajador['age'] > 18, DATA))
    print()
    print('Trabajadores mayores de 18 años: ')
    for trabajador in mayores_de_18:
        print(trabajador['name'])

    es_mayor = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    print()
    print('Valor nuevo: ')
    for trabajador in es_mayor:
        print(trabajador)
if __name__ == '__main__':
    run()














    #    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    # all_Platzi_workers = [worker["name"]
    #                       for worker in DATA if worker["organization"] == "Platzi"]
    # adults = [worker["name"] for worker in DATA if worker["age"] > 18]
    #

    # for worker in all_python_devs:
    #     print(worker)
