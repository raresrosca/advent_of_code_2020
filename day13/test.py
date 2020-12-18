

if __name__ == "__main__":
    schedule = [[7, 0], [13, 1], [59, 4], [31, 6], [19, 7]]
    counter = 0
    minute = 1068781
    if minute % schedule[0][0] == 0:
        print(minute, schedule[0][0])
        for i in schedule[1:]:
            #print(i)
            print(i[0] - minute % i[0], i[1])
            if i[0] - minute % i[0] == i[1]:
                counter += 1
    print(counter)