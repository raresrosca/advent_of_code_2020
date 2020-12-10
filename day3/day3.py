def handle_input(file_name):
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]

def solution_1(data, x, y):
    WIDTH, HEIGHT = len(data[0]), len(data)
    counter, w = 0, 0
    while True:
        for h in range(0, HEIGHT, y):
            if data[h][w%WIDTH] == '#':
                counter += 1
            w += x
        return counter


if __name__ == "__main__":
    data = handle_input("input.txt")
    print(solution_1(data, 3, 1))
    ans = solution_1(data, 1, 1)*solution_1(data, 3, 1)*solution_1(data, 5, 1)*solution_1(data, 7, 1)*solution_1(data, 1, 2)
    print(ans)


