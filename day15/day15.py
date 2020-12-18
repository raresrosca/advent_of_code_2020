def solution(rounds, starting_numbers):
    a = [0] * rounds
    for idx, i in enumerate(starting_numbers[:-1]):
        a[i] = idx+1

    pos = len(starting_numbers)
    init = starting_numbers[-1]

    while pos <= rounds:
        if a[init] == 0:
            initnew = 0
        else:
            initnew = pos - a[init]
        a[init] = pos
        init = initnew
        pos += 1
    return a.index(rounds)


if __name__ == "__main__":
    starting_numbers = [7,14,0,17,11,1,2]

    sol_1 = solution(2020, starting_numbers)
    sol_2 = solution(30000000, starting_numbers)
        
    print("Solution 1: ", sol_1)
    print("Solution 2: ", sol_2)
