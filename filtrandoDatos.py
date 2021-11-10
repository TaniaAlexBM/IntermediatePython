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
    # Obtener sólo los trabajadores que usan Python
    allPyDevs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    for worker in allPyDevs:
        print(worker)

    # Devs que trabajan en Platzi
    allPlatziDevs = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    for worker in allPlatziDevs:
        print(worker)

    # Todos los adultos
    adults = list(filter(lambda worker:worker['age'] > 18, DATA))
    for worker in adults:
        print(worker)
    adults1 = list(map(lambda worker:worker['name'], adults))
    for worker in adults1:
        print(worker)
    
    # Personas mayores
    oldPeople = list(map(lambda worker:worker | {'old': worker['age'] > 70}, DATA))
    # | pipe une un diccionario con un nuevo diccionario
    for worker in oldPeople:
        print(worker)


    # RETO
    all_python_devs = list(filter(lambda worker: worker['language'] == 'python', DATA))
    pyDevs = list(map(lambda worker: worker['name'], all_python_devs))
    for worker in pyDevs:
        print(worker) 
    
    all_Platzi_workers = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    platziDevs = list(map(lambda worker: worker['name'], all_Platzi_workers))
    for worker in platziDevs:
        print(worker)

    adults = [worker['name'] for worker in DATA if worker['age'] > 18]
    print(adults)

    old_people = [worker['name'] for worker in DATA if worker['age'] > 70]
    print(old_people)


if __name__ == '__main__':
    run()