def divisors(num):

    divisors = []

    for i in range(1, num + 1):

        if num % i == 0:

            divisors.append(i)

    return divisors


def run():
    num = input('Please, enter a number: ')
    
    #asserts that the condition is true, if it doesn't return a message
    assert num.isnumeric(), "you must enter a number"

    print(divisors(int(num)))


if __name__ == '__main__':
    run()


#in this i only practice try and except
def divisors(num):

    divisors = []

    for i in range(1, num + 1):

        if num % i == 0:

            divisors.append(i)

    return divisors


def run():
    try:
        num = input('Please, enter a number: ')
    
        #asserts that the condition is true, if it doesn't return a message
        assert num.isnumeric(), "you must enter a number"

        print(divisors(int(num)))
    except AssertionError:
        print('the number must be positive')


if __name__ == '__main__':
    run()
