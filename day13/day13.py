# ---- Part 1 -----

def handle_input(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        time_stamp = int(lines[0].rstrip())
        schedule = []
        for i in lines[1].split(','):
            if i != 'x':
                schedule.append(int(i))
        return time_stamp, schedule

def solution_1(time_stamp, schedule):
    minutes = []
    for i in schedule:
        minutes.append(i - time_stamp%i)
    return min(minutes), schedule[minutes.index(min(minutes))]

# ---- Part 2 ----- NOT IMPLEMENTED!!!!

def handle_input_2(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        time_stamp = int(lines[0].rstrip())
        schedule = []
        for index, i in enumerate(lines[1].split(',')):
            if i != 'x':
                schedule.append([int(i), index])
        return time_stamp, schedule

# def solution_2(schedule):
#     found = False
#     #minute = 667437230788118
#     #minute = 100000000000000
#     minute = 0
#     while not found:
#         counter = 0
#         if minute % schedule[0][0] == 0:
#             for i in schedule[1:]:
#                 if i[0] - minute % i[0] == i[1]:
#                     counter += 1
#                 else: 
#                     break
#             if counter == len(schedule) - 1:
#                 return minute
#         minute += 1

#         if minute % 1000000 == 0:
#             print(minute)

def solution_2(schedule):
    found = False
    minute = 100000000000000
    while not found:
        counter = 0
        if minute % schedule[0][0] == 0:
            for i in schedule[1:]:
                if i[0] - minute % i[0] == i[1]:
                    counter += 1
                else: 
                    break
            if counter == len(schedule) - 1:
                return minute
        minute += schedule[0][0]

        if minute % 1000000 == 0:
            print(minute)

    

if __name__ == "__main__":
    time_stamp, schedule = handle_input("input.txt")

    minutes, bus = solution_1(time_stamp, schedule)
    print("Solution 1: ", minutes * bus)

    _, schedule = handle_input_2("input.txt")
    print(schedule)
    print(len(schedule))

    print(solution_2(schedule))

    

