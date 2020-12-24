#Open data file
FILENAME = "data.txt"
file = open(FILENAME)
data = file.readlines()

#Part 1: find two that sum 2020, then multiply them
def find_two_sum_2020():
    for i in range(len(data)):
        n1 = int(data[i])
        for j in range(i+1,len(data)):
            n2 = int(data[j])
            if n1 + n2 == 2020:
                return n1 * n2
    return -1

print(find_two_sum_2020())

#Part 2: now find three, then multiply
def find_three_sum_2020():
    for i in range(len(data)):
        n1 = int(data[i])
        for j in range(i+1,len(data)):
            n2 = int(data[j])
            for k in range(j+1,len(data)):
                n3 = int(data[k])
                if n1 + n2 + n3 == 2020:
                    return n1 * n2 * n3
    return -1

print(find_three_sum_2020())
