def handle_input_1(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
        data = data.split('\n\n')
        return [''.join(data[i].split()) for i in range(len(data))]

def handle_input_2(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
        data = data.split('\n\n')
        return [data[i].split() for i in range(len(data))]

def solution_1(data):
    counter = 0
    for i in data:
        counter += len(set(i))
    return counter

def custom_intersection(myList):
    mySet = set(myList[0])
    for i in range(len(myList)):
        mySet = mySet.intersection(set(myList[i]))
    return len(mySet)

def solution_2(data):
    counter = 0
    for i in range(len(data)):
        counter += custom_intersection(data[i])

    return counter

if __name__ == "__main__":
    data = handle_input_1("input.txt")
    print("Solution for part 1: ", solution_1(data))
    
    data = handle_input_2("input.txt")
    print(data[0])
    print("Solution for part 2: ", solution_2(data))
