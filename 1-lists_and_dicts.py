def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {'firstname': 'Facundo', 'lastname': 'García'}

    super_list = [
        
        {'firstname': 'Facundo', 'lastname': 'García'},
        {'firstname': 'Emanuel', 'lastname': 'Juarez'},
        {'firstname': 'Juana', 'lastname': 'Perez'},
        {'firstname': 'Facundo', 'lastname': 'Garmendia'},
            ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 3, 0, 1],
        "floating_nums": [1.1, 4.55, 6.43],
    }

    for key, value in super_dict.items():
        print(key, '-', value)


if __name__ == '__main__':
    run()

