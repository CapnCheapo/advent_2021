with open("dataset1a.txt", "r") as items:
    filelines = items.readlines()
    filelines = [fileline.strip() for fileline in filelines]

count = len(filelines)
i = 0
previous = 0
current = 0
increased = 0

while i < count - 2:
    current = int(filelines[i]) + int(filelines[i+1]) + int(filelines[i+2])
    if current > previous:
        if i != 0:
            increased += 1
    previous = current
    i += 1

print(f"Increased: {increased}")