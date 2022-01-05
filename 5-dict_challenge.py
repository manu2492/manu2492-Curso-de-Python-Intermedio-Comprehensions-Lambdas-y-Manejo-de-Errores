#this dictionary comprehension creates an dictionary with all number from 1 to 100 and their square roots
def run():

    dict = {i: i**0.5 for i in range(1, 101)}

    print(dict)

if __name__ == '__main__':

    run()


