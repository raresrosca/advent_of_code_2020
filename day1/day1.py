from collections import OrderedDict

def handle_input(file_name):
    with open(file_name, 'r')  as f:
        return [int(line.strip()) for line in f.readlines()]

def solution_1(data):
    data = sorted(list(OrderedDict.fromkeys(data)))
    NEED = 2020
    i = 0
    k = len(data)-1
    while(True):
        if data[i] + data[k] == NEED:
            return data[i]*data[k]
        elif data[i]+data[k] > NEED:
            k -= 1
        else:
            i += 1

def solution_2(data):
    data = sorted(list(OrderedDict.fromkeys(data)))
    NEED = 2020
    for i, _ in enumerate(data):
        for j, _ in enumerate(data[i+1:]):
            if (NEED - data[i] - data[j]) in data:
                return data[i]*data[j]*(NEED - data[i] - data[j])


if __name__ == "__main__":
    data = handle_input("input.txt")
    print(solution_1(data))
    print(solution_2(data))