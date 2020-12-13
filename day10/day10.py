def handle_input(file_name):
    with open(file_name, 'r') as f:
        return [int(line.rstrip()) for line in f.readlines()]

def sol_1(data):
    c1, c2, c3 = 0, 0, 0
    for i in range(len(data)-1):
        diff = data[i+1] - data[i]
        if diff == 1:
            c1 += 1
        elif diff == 2:
            c2 +=1
        elif diff == 3:
            c3 +=1
        else:
            raise Exception("Corrupted data!")
    return c1, c2, c3

def sol_2(data, data_l, n):
    if n == data_l - 1:
        return 1
    if n in visited:
        return visited[n]
    ans = 0
    for i in range(n+1, data_l):
        if data[i] - data[n] <= 3:
            ans += sol_2(data, data_l, i)
    visited[n] = ans
    return ans

if __name__ == "__main__":
    data = handle_input("input.txt")
    data.append(0)
    data = sorted(data)
    data.append(data[-1]+3)

    c1, c2, c3= sol_1(data)
    print("Solution 1: ", c1*c3)

    visited = {}
    print("Solutions 2: ", sol_2(data, len(data), 0))
    