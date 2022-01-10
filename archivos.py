# OPEN FILES WITH 'r' AND 'w'

#this function open a file(number.txt) and creates an array(numbers) 
def read():
    numbers = []
    #'whit open' open the file, 'r' is the mode, this mean read, 'f' is the var name, who contains the 
    #file information
    with open("./files/numbers.txt", "r") as f: 
        for line in f:
            numbers.append(line)
    print(numbers)

#this function writes a txt file with the names in the array name
def write():
    names = ["Facundo", "Gregorio", "Marta", "Susana", "Jose"]
    with open("./files/name1.txt", "w") as f:
        for name in names: 
            f.write(name)
            f.write("\n")
    print(names)

def run():
    write()
    read()

if __name__ == '__main__':
    run()   
