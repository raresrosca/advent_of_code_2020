import re
from copy import deepcopy

def handle_input(file_name):
    with open(file_name, 'r') as f:
        l = []
        for line in f.readlines():
            if line[0:2] == 'ma':
                l.append(line.rstrip().split(' = '))
            if line[0:2] == 'me':
                l.append(re.findall('\d+', line))

    return l

# ----- Part 1 -----

def solution_1(data):
    memory_address = {}
    for item in data:
        if item[0] == 'mask':
            mask = item[1]
        else:
            bin_string = str("{0:b}".format(int(item[1])).zfill(36))
            to_memorize = ""
            for index, bit in enumerate(mask):
                if bit != 'X':
                    to_memorize += bit
                else:
                    to_memorize += bin_string[index]
            memory_address[int(item[0])] = int(to_memorize, 2)
    
    sum_values = 0
    for key, value in memory_address.items():
        sum_values += value

    return memory_address, sum_values

# ----- Part 2 -----

def solution_2(data):
    memory_address = {}
    for item in data:
        if item[0] == 'mask':
            mask = item[1]
        else:
            bin_string = str("{0:b}".format(int(item[0])).zfill(36))
            address_list = [""]

            for index, bit in enumerate(mask):
                if bit == '1':
                    for idx, _ in enumerate(address_list):
                        address_list[idx] += bit
                elif bit == '0':
                    for idx, _ in enumerate(address_list):
                        address_list[idx] += bin_string[index]
                else:
                    copy_list = deepcopy(address_list)
                    for idx, _ in enumerate(copy_list):
                        address_list.append(address_list[idx]+'0')
                        address_list[idx] += '1'
            
            for address in address_list:
                memory_address[int(address, 2)] = int(item[1])

    
    sum_values = 0
    for key, value in memory_address.items():
        sum_values += value

    return memory_address, sum_values
    

if __name__ == "__main__":
    data = handle_input("input.txt")

    memory_dictionary, sum_values = solution_1(data)
    print("Solution 1: ", sum_values)

    memory_dictionary, sum_values = solution_2(data)
    print("Solution 2: ", sum_values) 
