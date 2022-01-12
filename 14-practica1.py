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

    python_workers = []
    for i in DATA:
        if i['language'] == 'python':
            python_workers.append(i)
    for i in python_workers:
        print(i['name'])

    print(python_workers)
run()

#comprehension mode
def runc():
    all_python_devs = [worker for worker in DATA if worker["language"] == "python"]
    print(all_python_devs)
runc()

print('-------------------------2--------------------------------')

#this creates an array with all workers ages > 50
#then print all names
def run2():

    worker_ages = []
    for i in DATA:

        if i['age'] < 50:

            worker_ages.append(i)
    for i in worker_ages:
        print(i['name'])

run2()

#comprehension mode

def runc2():
    worker_agesc = [worker for worker in DATA if worker['age'] < 50]
    worker_agesc = [i['name'] for i in worker_agesc]
    print(worker_agesc)
runc2()





print('-------------------------3---------------------------------')
#this search for a backend developer
def run3():
    backend = []
    for i in DATA:
        if i['position'] == 'Backend Developer':
            backend.append(i)

    for i in backend:
        print(i['name'])

run3()

#comprehension mode
def run3c():
    backendc = [i for i in DATA if i['position'] == 'Backend Developer']
    print(backendc)
run3c()



print('-----------------------4-----------------------------------')
#this creates an array with names and languages per worker
def run4():
    names_language = []
    for i in DATA:
        names_language.append(i['language'])
        names_language.append(i['name'])

    print(names_language)

run4()

#comprehension mode
def runc4():
    names_languagec = [(i['language'], i['name']) for i in DATA]
    print(names_languagec)
runc4()


        
        































