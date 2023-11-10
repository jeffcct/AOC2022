contents = [i.split("\n") for i in (open("day_1/input.txt", "r").read().split("\n\n"))]
for i in range(len(contents)):
    for j in range(len(contents[i])):
        contents[i][j] = int(contents[i][j])

num_maxes = 3
max = [int("0") * num_maxes]
print(max)
for elf in contents:
    if sum(elf) > max[0]:
        max[2] = max[1]
        max[1] = max[0]
        max[0] = sum(elf)
print(sum(max))