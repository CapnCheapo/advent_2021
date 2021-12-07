
previous = -1
increased = 0

with open("dataset1a.txt", "r") as items:
    for item in items:
        if previous != -1:
            if int(item.strip()) > previous:
                increased += 1
        previous = int(item.strip())

print(increased)
