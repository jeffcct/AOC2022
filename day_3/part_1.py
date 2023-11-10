contents = [i for i in open("day_3/input.txt", "r").read().split("\n")]
for i in range(len(contents)):
    length = len(contents[i])
    contents[i] = [contents[i][:length // 2], contents[i][length // 2:]]
priorities = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = 0
for row in contents:
    for letter in row[0]:
        if letter in row[1]:
            total += priorities.index(letter)
            break
            
print(total)