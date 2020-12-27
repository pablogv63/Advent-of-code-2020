#Open data file
FILENAME = "data.txt"
file = open(FILENAME)
lines = file.readlines()
file.close()

#Part 1: check if passport has all fields
def checkPassport(passport):
    parts = passport.split(" ")[:-1]
    fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    found = 0
    for part in parts:
        key = part.split(":")[0]
        value = part.split(":")[1]
        if key in fields:
            found += 1
    return found >= 7

def checkPassports():
    valid = 0
    passport = ""
    #Extract a passport
    for line in lines:
        line = line.rstrip('\n')
        #if line not empty add to passport
        if len(line) != 0:
            passport += line + " "
        else:
            if checkPassport(passport):
                valid += 1
            passport = ""

    #Last check that for loop doesn't do
    if checkPassport(passport):
        valid += 1
    
    return valid

#Part 2: check with data validation
##hgt (Height) - a number followed by either cm or in:
##  If cm, the number must be at least 150 and at most 193.
##  If in, the number must be at least 59 and at most 76.
def checkHgt(height):
    if len(height) <= 2: return False
    unit = height[-2:]
    number = int(height[:-2])
    if unit == "cm":
        return number >= 150 and number <= 193
    #in
    elif unit == "in":
        return number >= 59 and number <= 76
    return False

##hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def checkHcl(color):
    if color[0] != "#" or len(color) != 7: return False
    color = color[1:]
    validChars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    for c in color:
        if c not in validChars:
            return False
    return True

##ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def checkEcl(color):
    validColors = ["amb","blu","brn","gry","grn","hzl","oth"]
    if color not in validColors:
        return False
    return True

##pid (Passport ID) - a nine-digit number, including leading zeroes.
def checkPid(pid):
    return len(pid) == 9 and pid.isnumeric()

##byr (Birth Year) - four digits; at least 1920 and at most 2002.
##iyr (Issue Year) - four digits; at least 2010 and at most 2020.
##eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
##cid (Country ID) - ignored, missing or not.
def checkField(key, value):
    switcher = {
        "byr": (lambda: len(value) == 4 and int(value) >= 1920 and int(value) <= 2002),
        "iyr": (lambda: len(value) == 4 and int(value) >= 2010 and int(value) <= 2020),
        "eyr": (lambda: len(value) == 4 and int(value) >= 2020 and int(value) <= 2030),
        "hgt": (lambda: checkHgt(value)),
        "hcl": (lambda: checkHcl(value)),
        "ecl": (lambda: checkEcl(value)),
        "pid": (lambda: checkPid(value)),
        "cid": (lambda: True)
        }
    return switcher.get(key, (lambda: False))()


def checkPassportWithValidation(passport):
    parts = passport.split(" ")[:-1]
    fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    found = 0
    for part in parts:
        key = part.split(":")[0]
        #Ignore cid
        if key == "cid": continue
        value = part.split(":")[1]
        if checkField(key,value):
            found += 1
    return found == 7

def checkPassportsWithValidation():
    valid = 0
    passport = ""
    #Extract a passport
    for line in lines:
        line = line.rstrip('\n')
        #if line not empty add to passport
        if len(line) != 0:
            passport += line + " "
        else:
            if checkPassportWithValidation(passport):
                valid += 1
            passport = ""

    #Last check that for loop doesn't do
    if checkPassportWithValidation(passport):
        valid += 1
    
    return valid

print(checkPassports())

print(checkPassportsWithValidation())
