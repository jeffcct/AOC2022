contents = [i for i in open("day_3/input.txt", "r").read().split("\n")]
priorities = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
total = 0
for i in range(0, len(contents), 3):
    for letter in contents[i]:
        if letter in contents[i + 1]:
            if letter in contents[i + 2]:
                total += priorities.index(letter)
                break

print(total)