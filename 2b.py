horiz = 0
depth = 0
aim = 0

with open("dataset2b.txt", "r") as items:
    filelines = items.readlines()
    filelines = [fileline.strip() for fileline in filelines]

for line in filelines:
    (command, extent) = line.split(" ")
    if command == "forward":
        horiz = horiz + int(extent)
        depth = depth + (int(extent) * aim)
    elif command == "down":
        aim = aim + int(extent)
    elif command == "up":
        aim = aim - int(extent)

print(f"Horizontal position: {horiz}")
print(f"Depth: {depth}")
print(f"Aim: {aim}")
print(f"Thing google wants: {horiz * depth}")