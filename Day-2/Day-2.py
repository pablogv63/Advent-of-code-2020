#Open data file
FILENAME = "data.txt"
file = open(FILENAME)
data = file.readlines()

#Part 1: check if valid passwords
def is_valid_part_1(min,max,letter,password):
    password = password.rstrip('\n')
    #At least min, at most max
    occurences = password.count(letter)
    if occurences >= min and occurences <= max:
        return True
    return False

def check_passwords_part_1():
    valid = 0
    for line in data:
        parts = line.split(" ")
        #Min and max
        minMax = parts[0].split("-")
        min = int(minMax[0])
        max = int(minMax[1])
        #letter
        letter = parts[1][0]
        #str
        password = parts[2]
        #Check
        if is_valid_part_1(min,max,letter,password):
            valid += 1
    return valid

print(check_passwords_part_1())

#Part 2: check if valid, change rules
def is_valid_part_2(first,second,letter,password):
    password = password.rstrip('\n')
    first -= 1
    second -= 1
    #Found in first, not in second
    found_first = (letter == password[first])
    found_second= (letter == password[second])
    return found_first != found_second

def check_passwords_part_2():
    valid = 0
    for line in data:
        parts = line.split(" ")
        #Min and max
        fstSnd = parts[0].split("-")
        first = int(fstSnd[0])
        second = int(fstSnd[1])
        #letter
        letter = parts[1][0]
        #str
        password = parts[2]
        #Check
        if is_valid_part_2(first,second,letter,password):
            valid += 1
    return valid

print(check_passwords_part_2())
