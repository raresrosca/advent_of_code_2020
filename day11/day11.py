from copy import deepcopy

def handle_input(file_name):
    with open(file_name, 'r') as f:
        return [[i for i in line.rstrip()] for line in f.readlines()]

def change_status(layout, x, y):
    counter = 0
    isEmpty = False
    if layout[x][y] == '.':
        return layout[x][y], False
    elif layout[x][y] == 'L':
        isEmpty = True
    else:
        isEmpty = False

    for i in range(max(x-1, 0), min(x+2, len(layout))):
        for j in range(max(y-1,0), min(y+2, len(layout[0]))):  
            if layout[i][j] == '#':
                counter +=1

    if isEmpty == True and counter == 0:
        return '#', True
    elif isEmpty == False and counter >= 5:
        return 'L', True
    else:
        return layout[x][y], False
                
def sol_1(seat_layout):
    ex_map = []
    continue_operation = True
    while continue_operation:
        continue_operation = False
        ex_map = deepcopy(seat_layout)
        for x in range(len(seat_layout)):
            for y in range(len(seat_layout[0])):
                seat_layout[x][y], hasChanged = change_status(ex_map, x, y)
                if hasChanged:
                    continue_operation = True

    
    return seat_layout

        


if __name__ == "__main__":
    data = handle_input("input.txt")
    print(len(data), len(data[0]))
    occupied = 0
    final_layout = sol_1(data)
    for i in range(len(final_layout)):
        for j in range(len(final_layout[0])):
            if final_layout[i][j] == '#':
                occupied += 1
    print("Solution 1: ", occupied)