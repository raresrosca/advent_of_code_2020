def handle_input(file_name):
    data = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            y = line.split()
            data.append([y[0].split('-'), y[1][0], y[2]])
    return data

def solution_1(data):
    counter = 0
    for item in data:
        if item[2].count(item[1]) >= int(item[0][0]) and item[2].count(item[1]) <= int(item[0][1]):
            counter += 1
    return counter

def solution_2(data):
    counter = 0
    for item in data:
        start = int(item[0][0])-1
        end = int(item[0][1])-1
        try:
            if (item[2][start] == item[1]) != (item[2][end] == item[1]):
                counter += 1
        except IndexError:
            pass
    return counter


if __name__ == "__main__":
    data = handle_input("input.txt")
    print(solution_1(data))
    print(solution_2(data))