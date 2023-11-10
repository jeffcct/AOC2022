
contents = [i.split() for i in open("day_2/input.txt", "r").read().split("\n")]
total = 0
for line in contents:
    if line[0] == "A":
        if line[1] == "X":
            total += 3
        elif line[1] == "Y":
            total += 4
        elif line[1] == "Z":
            total += 8
    elif line[0] == "B":
        if line[1] == "X":
            total += 1
        elif line[1] == "Y":
            total += 5
        elif line[1] == "Z":
            total += 9
    elif line[0] == "C":
        if line[1] == "X":
            total += 2
        elif line[1] == "Y":
            total += 6
        elif line[1] == "Z":
            total += 7
            
print(total)
