my_list = [2,2,2,2,2]

all_mulplied = 1

for i in my_list:
    all_mulplied = all_mulplied * i

print(all_mulplied)

#list comprehension mode

all_mulplied2 = [i * i for i in my_list]

print(all_mulplied2)

#random code
l = [1, 2, 3, 4, 5]
l[:] = [x * 5 for x in l]

print(l)

