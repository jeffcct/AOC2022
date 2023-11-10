import math

def draw_line(map, pos1, pos2, char):
    if pos1[0] == pos2[0]:
        length = pos2[1] - pos1[1]
        dir = int((length) / abs(length))
        for i in range(abs(length) + 1):
            map[pos1[1] + i * dir][pos1[0]] = char
    else:
        length = pos2[0] - pos1[0]
        dir = int((length) / abs(length))
        for i in range(abs(length) + 1):
            map[pos1[1]][pos1[0] + i * dir] = char
    
            
        
    
    

def initialize(min, max):
    return [["." for i in range(max[0] - min[0] + 1)] for j in range(max[1] - min[1] + 1)]
    
    
input_file = open("day_14/input.txt", "r")
contents = input_file.read().split("\n")
input_file.close()

minimum = [250, 0]
maximum = [750, 0]
for i in range(len(contents)):
    contents[i] = contents[i].split(" -> ")
    for j in range(len(contents[i])):
        contents[i][j] = contents[i][j].split(",")
        contents[i][j][0] = int(contents[i][j][0])
        contents[i][j][1] = int(contents[i][j][1])
    
        if minimum[0] > contents[i][j][0]:
            minimum[0] = contents[i][j][0]
        elif maximum[0] < contents[i][j][0]:
            maximum[0] = contents[i][j][0]
        if minimum[1] > contents[i][j][1]:
            minimum[1] = contents[i][j][1]
        elif maximum[1] < contents[i][j][1]:
            maximum[1] = contents[i][j][1]
            
maximum[1] += 4
       
            
for line in contents:
    for position in line:
        position[0] -= minimum[0]
        position[1] -= minimum[1]
print(maximum, minimum)

map = initialize(minimum, maximum)

for line in contents:
    for i in range(len(line) - 1):
        draw_line(map, line[i], line[i + 1] , "#")

position =  [500 - minimum[0], 0]

num = 0
while map[position[1]][position[0]] == ".":
    pos = position.copy()
    while True: 
        if pos[1] + 1 >= maximum[1]:
            map[pos[1]][pos[0]] = "+"
            break
            
        if map[pos[1] + 1][pos[0]] == ".":
            pos = [pos[0], pos[1] + 1]
        elif map[pos[1] + 1][pos[0] - 1] == ".":
            pos = [pos[0] - 1, pos[1] + 1]
        elif map[pos[1] + 1][pos[0] + 1] == ".":
            pos = [pos[0] + 1, pos[1] + 1]
        else:
            map[pos[1]][pos[0]] = "+"
            break
    num += 1

for line in map:
    for letter in line:
        print(letter, end = "")
    print()

print(num)

            

