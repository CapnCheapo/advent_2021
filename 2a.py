horiz = 0
depth = 0

with open("dataset2b.txt", "r") as items:
    filelines = items.readlines()
    filelines = [fileline.strip() for fileline in filelines]

for line in filelines:
    (command, extent) = line.split(" ")
    if command == "forward":
        horiz = horiz + int(extent)
    elif command == "down":
        depth = depth + int(extent)
    elif command == "up":
        depth = depth - int(extent)

print(f"Horizontal position: {horiz}")
print(f"Depth: {depth}")
print(f"Thing google wants: {horiz * depth}")