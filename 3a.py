with open("dataset3b.txt", "r") as items:
    filelines = items.readlines()
    filelines = [fileline.strip() for fileline in filelines]

gamma = ""
epsilon = ""

for i in range(len(filelines[0])):
    zeroes = 0
    ones = 0
    for line in filelines:
        if line[i] == '0':
            zeroes += 1
        elif line[i] == '1':
            ones += 1
    if ones > zeroes:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

power = int(gamma, 2) * int(epsilon, 2)
print(power)