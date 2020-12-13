from copy import deepcopy

def handle_input(file_name):
    with open(file_name, 'r') as f:
        return [[i for i in line.rstrip()] for line in f.readlines()]

def change_status(original_map):
    copy_map = deepcopy(original_map)
    for x in range(len(copy_map)):
        for y in range(len(copy_map[0])):
            for i in range(max(x-1, 0), min(x+2, len(copy_map))):
                for j in range(max(y-1,0), min(y+2, len(copy_map[0]))): 



if __name__ == "__main__":
    data = handle_input("input.txt")
    print(len(data), len(data[0]))