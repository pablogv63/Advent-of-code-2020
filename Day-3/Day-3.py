#Open data file
FILENAME = "data.txt"
file = open(FILENAME)
data = file.readlines()

#Part 1: check path right 3, down 1
def check_path(right, down):
    i,j = 0,0
    trees = 0
    colLen = len(data[0]) - 1 # Ignore /n

    while i in range(len(data)):
        #Trunk column
        j = j % colLen
        #Find tree
        if data[i][j] == "#":
            trees += 1
        #Slope
        i += down
        j += right
    return trees

print(check_path(3,1))

#Part 2: check various paths
def check_paths():
    first   = check_path(1,1)
    second  = check_path(3,1)
    third   = check_path(5,1)
    fourth  = check_path(7,1)
    fifth   = check_path(1,2)
    return first * second * third * fourth * fifth

print(check_paths())
