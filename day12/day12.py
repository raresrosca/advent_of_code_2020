def handle_input(file_name):
    with open(file_name, 'r') as f:
        return [[line[0], line[1:].rstrip()] for line in f.readlines()]

def solution_1(instructions):
    orientation = [0, 1, 2, 3] #right, up, left, down
    idx_orientation = 0
    x, y = 0, 0
    for index, instruction in enumerate(instructions):
        if instruction[0] == 'E':
            x += int(instruction[1])
        if instruction[0] == 'N':
            y += int(instruction[1])
        if instruction[0] == 'W':
            x -= int(instruction[1])
        if instruction[0] == 'S':
            y -= int(instruction[1])
        if instruction[0] == 'F':
            if orientation[idx_orientation] == 0:
                x += int(instruction[1])
            elif orientation[idx_orientation] == 1:
                y += int(instruction[1])
            elif orientation[idx_orientation] == 2:
                x -= int(instruction[1])
            elif orientation[idx_orientation] == 3:
                y -= int(instruction[1])
        if instruction[0] == 'L':
            idx_orientation += int(instruction[1])/90
            idx_orientation = idx_orientation%4
        if instruction[0] == 'R':
            idx_orientation -= int(instruction[1])/90
            idx_orientation = idx_orientation%4

    return x, y

def solution_2(instructions):
    sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)
    way_x = 10
    way_y = 1
    x, y = 0, 0
    for index, instruction in enumerate(instructions):
        if instruction[0] == 'E':
            way_x += int(instruction[1])
        if instruction[0] == 'N':
            way_y += int(instruction[1])
        if instruction[0] == 'W':
            way_x -= int(instruction[1])
        if instruction[0] == 'S':
            way_y -= int(instruction[1])
        if instruction[0] == 'F':
            x += way_x*int(instruction[1])
            y += way_y*int(instruction[1])
        if (instruction[0] == 'L' and instruction[1] == '90') or (instruction[0] == 'R' and instruction[1] == '270'):
            copy_x = way_x
            way_x = (-1)*way_y
            way_y = sign(copy_x)*abs(copy_x)
        if(instruction[0] == 'L' and instruction[1] == '180') or (instruction[0] == 'R' and instruction[1] == '180'):
            way_x = -way_x
            way_y = -way_y
        if(instruction[0] == 'L' and instruction[1] == '270') or (instruction[0] == 'R' and instruction[1] == '90'):
            copy_x = way_x
            way_x = sign(way_y)*abs(way_y)
            way_y = (-1)*copy_x
        print("Ship position: ", x, y)
        print("Waypoint position: ", way_x, way_y)
    
    return x, y

if __name__ == "__main__":
    data = handle_input("input.txt")
    x, y = solution_1(data)

    print("Solution 1: ", abs(x)+ abs(y))

    x, y = solution_2(data)
    print("Solution 1: ", abs(x)+ abs(y))