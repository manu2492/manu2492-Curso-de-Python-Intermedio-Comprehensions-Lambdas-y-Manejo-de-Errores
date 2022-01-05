#this lambda creates an array with all multiples of 4, 6 and 9 from 1 to 1000
def run():

    arr = [i for i in range(1, 1001) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

    print(arr)

run()

