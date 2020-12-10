def handle_input(file_name):
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]

def calculate_row(ticket):
    ticket = ticket[:-3]
    start, end = 0, 127
    mid = start + (end - start) // 2
    for i in ticket:
        if i == "F":
            end = mid 
            mid = start + (end - start) // 2 
        elif i == "B":
            start = mid + 1 
            mid = start + (end - start) // 2 

    return mid


def calculate_column(ticket):
    ticket = ticket[-3:]
    start, end = 0, 7
    mid = start + (end - start) / 2 
    for i in ticket:
        if i == "L":
            end = mid 
            mid = start + (end - start) / 2 
        elif i == "R":
            start = mid + 1 
            mid = start + (end - start) / 2 

    return mid

# Bad solution, would not recommend 2/10

if __name__ == "__main__":
    tickets = handle_input("input.txt")
    MAX = -1
    seats, ids = [], []
    for ticket in tickets:
        ids.append(calculate_row(ticket)*8 + calculate_column(ticket))
        if (calculate_row(ticket)*8 + calculate_column(ticket)) >= MAX:
            MAX = (calculate_row(ticket)*8 + calculate_column(ticket))
    print(MAX)

    for ticket in tickets: 
        seats.append([calculate_row(ticket), calculate_column(ticket)])

    for i in range(128): 
        for j in range(8):
            if [i, j] not in seats and (i*8+j)-1 in ids and (i*8+j)+1 in ids:
                print(i*8+j)


