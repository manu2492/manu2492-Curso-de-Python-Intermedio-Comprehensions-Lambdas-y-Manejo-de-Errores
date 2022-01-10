def run(number):

    divisors = []

    for i in range(1, number + 1):

        if number % i == 0:

            print(i)    
            divisors.append(i)

    print(divisors)











if __name__ == '__main__':
    run(10)

