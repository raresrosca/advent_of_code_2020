def handle_input(file_name):
    with open(file_name, 'r') as f:
        return [int(line.rstrip()) for line in f.readlines()]

def isSum(number, preamble):
    for i in range(len(preamble)):
        for j in range(i, len(preamble)):
            if preamble[i]+preamble[j] == number:
                return True

def solution_1(data, past):
    for idx in range(past, len(data)):
        if isSum(data[idx], data[idx-past:idx]):
            pass
        else:
            return data[idx]

# Part 2 is basically finding a subarray with a given sum

def solution_2(data, ans):
    for i in range(len(data)):
        for j in range(i, len(data)):
            if sum(data[i:j]) == ans:
                return sorted(data[i:j])[0]+sorted(data[i:j])[-1]
            elif sum(data[i:j]) > ans:
                break
            else:
                pass



if __name__ == "__main__":
    data = handle_input("input.txt")
    ans1 = solution_1(data, 25)
    print("Solution 1: ", ans1)
    ans2 = solution_2(data, ans1)
    print("Solution 1: ", ans2)