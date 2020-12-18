from copy import deepcopy

def handle_input(file_name):
    with open(file_name, 'r') as f:
        return [[i for i in line.rstrip()] for line in f.readlines()]

# ---- Part 1 -----

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
                
def solution_1(seat_layout):
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

# ---- Part 2 ----

def change_status_2(layout, y, x):
    counter = 0
    isEmpty = False
    if layout[y][x] == '.':
        return layout[y][x], False
    elif layout[y][x] == 'L':
        isEmpty = True
    else:
        isEmpty = False

    counter += check_sides(layout, y, x)
    counter += check_diagonals(layout, y, x)

    if isEmpty == True and counter == 0:
        return '#', True
    elif isEmpty == False and counter >= 5:
        return 'L', True
    else:
        return layout[y][x], False

def check_sides(layout, y, x):
    counter = 0
    for i in range(min(x+1, len(layout[0])), len(layout[0])): #right
        if layout[y][i] == '#':
            counter += 1
            break
        elif layout[y][i] == 'L':
            break
        else:
            pass

    for i in range(max(x-1, -1), -1, -1): #left
        if layout[y][i] == '#':
            counter += 1
            break
        elif layout[y][i] == 'L':
            break
        else:
            pass

    for i in range(min(y+1, len(layout)), len(layout)): #down
        if layout[i][x] == '#':
            counter += 1
            break
        elif layout[i][x] == 'L':
            break
        else:
            pass

    for i in range(max(y-1, -1), -1, -1): #up
        if layout[i][x] == '#':
            counter += 1
            break
        elif layout[i][x] == 'L':
            break
        else:
            pass
    
    return counter


def check_diagonals(layout, y, x):
    counter = 0

    # First qudrant diagonal
    i = min(x+1, len(layout[0]))
    j = max(y-1, -1)
    while i < len(layout[0]) and j >= 0: 
        if layout[j][i] == '#':
            counter += 1
            break
        elif layout[j][i] == 'L':
            break
        else:
            i += 1
            j -= 1


    # Second quadrant diagonal
    i = max(x-1, -1)
    j = max(y-1, -1)
    while i >= 0 and j >= 0: 
        if layout[j][i] == '#':
            counter += 1
            break
        elif layout[j][i] == 'L':
            break
        else:
            i -= 1
            j -= 1

    # Third quadrant diagonal
    i = max(x-1, -1)
    j = min(y+1, len(layout))
    while i >= 0 and j < len(layout): 
        if layout[j][i] == '#':
            counter += 1
            break
        elif layout[j][i] == 'L':
            break
        else:
            i -= 1
            j += 1

    # Forth quadrant diagonal 
    i = min(x+1, len(layout[0]))
    j = min(y+1, len(layout))
    while i < len(layout[0]) and j < len(layout): 
        if layout[j][i] == '#':
            counter += 1
            break
        elif layout[j][i] == 'L':
            break
        else:
            i += 1
            j += 1

    return counter 


def solution_2(seat_layout):
    continue_operation = True
    while continue_operation:
        continue_operation = False
        ex_map = deepcopy(seat_layout)
        for y in range(len(seat_layout)):
            for x in range(len(seat_layout[0])):
                seat_layout[y][x], hasChanged = change_status_2(ex_map, y, x)
                if hasChanged:
                    continue_operation = True
    
    return seat_layout
    

if __name__ == "__main__":
    data = handle_input("input.txt")
    #print(len(data), len(data[0]))
    occupied = 0
    # final_layout = sol_1(data)
    final_layout = solution_2(data)
    for i in range(len(final_layout)):
        for j in range(len(final_layout[0])):
            if final_layout[i][j] == '#':
                occupied += 1
    print(change_status_2(data, 1, 2))
    print("Solution 2: ", occupied)