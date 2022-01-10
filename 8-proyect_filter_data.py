
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
    #this array only returns python devs
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]

    for worker in all_python_devs:
        print(worker)

    print('---------------platzi workers-------------------')
    

    #this array only returns platzi workers
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi' ]

    for worker in all_platzi_workers:
        print(worker)


    print('----------------Adults-----------------------------')
    #this returns all the dictionaries with age > 18, but it's a lot of text, so we used map to filter
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))
    print(adults)


    print('-----------------Olds------------------------------')
    #this returns all the people > 70
    olds = list(filter(lambda worker: worker['age'] > 70, DATA))
    olds = list(map(lambda worker: worker['name'], olds))
    print(olds)

    
    #another way to do what is up
    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))
    for worker in old_people:
        print(worker)













if __name__ == '__main__':
    run()

