def run():

    list1 = [1, 2, 3, 4, 5]
    list2 = []
    for i in list1:

        i = i**2
        list2.append(i)

    print(list2)

if __name__ == '__main__':
    run()


#lists comprehension mode
list3 = [1, 2, 3, 4, 5]

list4 = [i**2 for i in list3]

print(list4)

