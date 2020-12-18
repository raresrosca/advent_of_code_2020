import re 

def handle_input(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        fields = []
        tickets = []
        for i in range(20):
            fields.append(re.findall('\d+', lines[i]))
        
        for i in lines[25:]:
            tickets.append(re.findall('\d+', i))

        my_ticket = re.findall('\d+', lines[22])

        return fields, my_ticket, tickets

# def handle_input(file_name):
#     with open(file_name, 'r') as f:
#         lines = f.readlines()
#         fields = []
#         tickets = []
#         for i in range(3):
#             fields.append(re.findall('\d+', lines[i]))
        
#         for i in lines[8:]:
#             tickets.append(re.findall('\d+', i))

#         my_ticket = re.findall('\d+', lines[5])

#         return fields, my_ticket, tickets


def is_valid(item, fields):
    isValid = False
    for field in fields:
        if int(field[0]) <= item <= int(field[1]) or int(field[2]) <= item <= int(field[3]):
            isValid = True
        else:
            pass
    return isValid

def solution_1(fields, tickets):
    error_rate = 0
    for idx, ticket in enumerate(tickets):
        for item in ticket:
            if is_valid(int(item), fields):
                pass
            else:
                error_rate += int(item)
                
    return error_rate

def filter_invalid_tickets(fields, tickets):
    
    for idx, ticket in enumerate(tickets):
        validTicket = True
        for item in ticket:
            if is_valid(int(item), fields):
                pass
            else:
                validTicket = False
        if not validTicket:
            tickets.remove(ticket)
                
    return tickets

if __name__ == "__main__":
    fields, my_ticket, tickets = handle_input("input.txt")
    
    error_rate = solution_1(fields, tickets)
    print("Solution 1: ", error_rate)