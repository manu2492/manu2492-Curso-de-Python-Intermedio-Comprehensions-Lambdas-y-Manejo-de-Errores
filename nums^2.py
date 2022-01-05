# new version of 2-nums, but in this array only will be the numbers who can be divisible by 3
def run():

    arr = [] 


    for i in range(0, 10):
        i = i**2

        if i % 3 == 0:

            arr.append(i)

    print(arr)

run()
