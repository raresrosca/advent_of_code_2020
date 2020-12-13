import re

# ---- Part 1 ----

#Without the number of bags -- For part 1

def handle_input_1(file_name): #outputs a list of lists, where the first element is the parent and the others are the children, no spaces
    with open(file_name, 'r') as f:
        return [re.split('bagscontain|bag.$|bags.$|bag,|bags,', ''.join([i.strip() for i in line if not i.isdigit()]))[:-1] for line in f.readlines()]

def process_input_1(data):
    colors_dictionary = {}

    for rule in data:
        for j in range(1, len(rule)):
            if rule[j] not in colors_dictionary:
                colors_dictionary[rule[j]] = [rule[0]]
            else:
                if not isinstance(colors_dictionary[rule[j]], list):
                    colors_dictionary[rule[j]] = [colors_dictionary[rule[j]]]
                colors_dictionary[rule[j]].append(rule[0])
    return colors_dictionary

def recursive_1(colors_dictionary, item, counter, visited):
    if item in visited:
        return False
    if item not in colors_dictionary:
        visited.append(item)
        return False

    visited.append(item)
    for i in colors_dictionary[item]:
        recursive_1(colors_dictionary, i, counter, visited) 
    return len(visited)

# ---- Part 2 ----

# Inclues the number of bags 

def handle_input_2(file_name):
    with open(file_name, 'r') as f:
        return [re.split(' bags contain | bag.$| bags.$| bag, | bags, ', line.rstrip())[:-1] for line in f.readlines()]


def process_input_2(data):
    colors_dictionary = {}

    for rule in data:
        colors_dictionary[rule[0]] = {}
        for j in range(1, len(rule)):
            if rule[j] != 'no other':
                colors_dictionary[rule[0]][rule[j][2:]] = int(rule[j][0])
            else:
                pass
    return colors_dictionary

my_array = []

def recursive_2(colors_dictionary, item):
    global my_array
    for child in colors_dictionary[item]:
        n = child
        q = int(colors_dictionary2[item][child])
        for x in range(q):
            my_array.append(i for i in recursive_2(colors_dictionary, n))
    return my_array

if __name__ == "__main__":
    data1 = handle_input_1("input.txt")
    colors_dictionary1 = process_input_1(data1)
    ans_1 = recursive_1(colors_dictionary1, 'shinygold', 0, []) -1 # -1 for the 'shinygold' bag itself
    print('Solution 1: ', ans_1)

    data2 = handle_input_2("input.txt")
    colors_dictionary2 = process_input_2(data2)
    print(len(recursive_2(colors_dictionary2, "shiny gold")))

