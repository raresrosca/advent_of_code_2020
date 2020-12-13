def handle_input(file_name):
    with open(file_name, 'r') as f:
        return [line.split() for line in f.readlines()]

# ---- Part 1 ----

def solution_1(code):
    visited = [0 for i in range(len(code))]
    accumulator = 0
    idx = 0
    while(visited[idx] != 1):
        visited[idx] = 1
        if code[idx][0] == 'acc':
            accumulator += int(code[idx][1])
            idx +=1
        elif code[idx][0] == 'jmp':
            idx += int(code[idx][1])
        else:
            idx +=1
    return accumulator

# ---- Part 2 ----

def flip_instruction(instruction):
    if instruction == 'acc':
        return instruction
    elif instruction == 'jmp':
        return 'nop'
    elif instruction == 'nop':
        return 'jmp'


def solution_2(code):
    final_idx = len(code)-1
    for i in range(len(code)):
        code[i][0] = flip_instruction(code[i][0])
        visited = [0 for j in range(len(code))]
        accumulator = 0
        idx = 0
        while(visited[idx] != 1):
            visited[idx] = 1
            if code[idx][0] == 'acc':
                accumulator += int(code[idx][1])
                idx +=1
            elif code[idx][0] == 'jmp':
                idx += int(code[idx][1])
            else:
                idx +=1
            if idx == final_idx:
                return accumulator
        code[i][0] = flip_instruction(code[i][0])



if __name__ == "__main__":
    game_code = handle_input("input.txt")
    accumulator_value = solution_1(game_code)
    print("Solution 1: ", accumulator_value)


    print("Solution 2: ", solution_2(game_code))

