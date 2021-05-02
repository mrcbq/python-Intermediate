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
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python'] #Usando comprehension
    print('all_python_devs usando comprehesion son:', all_python_devs, '\n')

    all_python_devs1 = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs1 = list(map(lambda worker: worker['name'], all_python_devs1))
    print('all_python_devs usando High Order Functions son:', all_python_devs, '\n') #Usando High Order Functions (HFO)
    
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi'] #Usando comprehension
    print('all_platzi_workers usando comprehension son:', all_platzi_workers, '\n') 
    all_platzi_workers1 = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_workers1 = list(map(lambda worker: worker['name'], all_platzi_workers1))
    print('all_platzi_workers usando High Order Functions son:', all_platzi_workers1, '\n')


    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))
    print('adults usando High Order Functions son:', adults, '\n')
    adults = [worker['name'] for worker in DATA if worker['age'] > 18]
    print('adults usando comprehension son:', adults, '\n')

    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))
    old_people = [worker['name'] for worker in old_people if worker['old']]
    print('old_people usando comprehension y High Order Functions son:', old_people, '\n')


    # for worker in old_people:
    #     print(worker)

if __name__ == '__main__':
    run()