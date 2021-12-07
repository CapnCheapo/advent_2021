with open("dataset3b.txt", "r") as items:
    filelines = items.readlines()
    filelines = [fileline.strip() for fileline in filelines]

work = filelines.copy()
for i in range(len(work[0])):
    zeroholder = []
    oneholder = []
    if len(work) > 1:
        for line in work:
            if line[i] == '0':
                zeroholder.append(line)
            elif line[i] == '1':
                oneholder.append(line)
        if len(zeroholder) > len(oneholder):
            work = zeroholder
        else:
            work = oneholder
    oxygen = int(work[0], 2)

work = filelines.copy()
for i in range(len(work[0])):
    zeroholder = []
    oneholder = []
    if len(work) > 1:
        for line in work:
            if line[i] == '0':
                zeroholder.append(line)
            elif line[i] == '1':
                oneholder.append(line)
        if len(zeroholder) > len(oneholder):
            work = oneholder
        else:
            work = zeroholder
    co2 = int(work[0], 2)

print(f"Life support rating: {oxygen * co2}")
