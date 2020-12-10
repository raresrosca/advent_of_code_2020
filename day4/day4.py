import re

def handle_input(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
        data = data.split('\n\n')
        return [data[i].split() for i in range(len(data))]

def solution_1(data):
    req_fields = []
    counter = 0
    for person in data:
        temp = []
        for field in person:
            temp.append(field.split(':')[0])
        req_fields.append(temp)
        temp = []
    for check in req_fields:
        if len(check) == 8:
            counter += 1
        elif len(check) == 7 and 'cid' not in check:
            counter += 1
        else:
            pass
    return counter

def solution_2(data):
    req_fields = []
    counter = 0
    for person in data:
        my_dict = {}
        for field in person:
            my_dict[field.split(':')[0]] = field.split(':')[1]
        req_fields.append(my_dict)
        my_dict = {}
    # for check in req_fields:
    #     if(len(check) == 8):
    #         counter += is_valid(check)
    #     elif (len(check) == 7) and ('cid' not in check):
    #         counter += is_valid(check)
    #     else:
    #         pass
    mandatory_fields = ['byr' ,'iyr' ,'eyr' ,'hgt' ,'hcl' ,'ecl' ,'pid']
    for check in req_fields:
        a = 1
        for f in mandatory_fields:
            if f not in check:
                a = 0
        if a == 0:
            pass
        else:
            counter+= is_valid(check)
    return counter

def is_valid(check):
    if not re.findall("^\d{9}$", check['pid']):
        return 0
    if check['ecl'] not in ['amb', 'blu', 'brn','gry','grn','hzl','oth']:
        return 0
    if re.match(r'^\#[0-9a-f]{6}$', check['hcl']) is None:
        return 0
    if not (1920 <= int(check['byr']) <= 2002):
        return 0
    if not (2010 <= int(check['iyr']) <= 2020): 
        return 0
    if not (2020 <= int(check['eyr']) <= 2030):
        return 0
    if 'cm' in check['hgt'] and not (150 <= int(check['hgt'][:-2]) <= 193):
        return 0
    if 'in' in check['hgt'] and not (59 <= int(check['hgt'][:-2]) <= 76):
        return 0
    if 'cm' not in check['hgt'] and 'in' not in check['hgt']:
        return 0
    return 1

if __name__ == "__main__":
    data = handle_input("input.txt")
    print("Part 1 solution: ", solution_1(data))
    print("Part 2 solution: ", solution_2(data))