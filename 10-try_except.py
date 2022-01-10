
def divisors(number):

    divisors_l = []

    for i in range(1, number + 1):

        if number % i == 0:

            divisors_l.append(i)

    print(divisors)

def run():
    try:
        number = int(input('enter a number: '))

        print(divisors_l)
    
    except ValueError:

        print('it only work with numbers')


if __name__ == '__main__':
    run()
