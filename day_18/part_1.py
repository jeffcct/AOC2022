def create_vector(dir):
    if dir == "<":
        return [-1, 0]
    elif dir == ">":
        return [1, 0]
    else:
        return [0, -1]


def move(grid, pos, shape, dir, width):
    new_pos = create_vector(dir)
    for dp in shape:
        x = pos[0] + dp[0] + new_pos[0]
        y = pos[1] + dp[1] + new_pos[1]
        if x == width or x == -1:
            return False
        if y == 0:
            return False 
        if grid[(x, y)] != '.':
            return False
    return True


def add_shape(grid, shape, pos):
    for dp in shape:
        grid[(pos[0] + dp[0], pos[1] + dp[1])] = "#"
        
        
def get_max(shape, pos):
    maximum = 0
    for dp in shape:
        if pos[1] + dp[1] > maximum:
            maximum = pos[1] + dp[1]
    return maximum
            
            
def print_grid(grid):
    print(".........")
    for x in range(grid["size"][0]):
        for y in range(grid["size"][1]):
            if grid[(x, y)] == ".":
                print(" ", end = "")
            else:
                print(grid[(x, y)], end = "")
        print()
                

input_file = open("day_18/input.txt", "r")
instructions = input_file.read()
input_file.close()

shapes = []
shapes.append(((0, 0), (1, 0), (2, 0), (3, 0),))
shapes.append(((0, 1), (1, 0), (1, 1), (2, 1), (1, 2),))
shapes.append(((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),)
shapes.append(((0, 0), (0, 1), (0, 2), (0, 3)),)
shapes.append(((0, 0), (0, 1), (1, 0), (1, 1)),)

num_shapes = len(shapes)

grid = {"size": [7, 5000]}
for x in range(7):
    for y in range(5000):
        grid[(x, y)] = '.'


width = 7
maximum = 0
shape_index = 0
direction_index = 0
num_rocks = 0

pos = [2, 4]

while num_rocks < 2022:
    direction = instructions[direction_index % len(instructions)]
    direction_index += 1
    #moves left / right
    if move(grid, pos, shapes[shape_index], direction, width):
        if direction == "<":
            pos[0] -= 1
        else:
            pos[0] += 1
    
    #moves down
    direction = "v"
    if move(grid, pos, shapes[shape_index], direction, width):
        pos[1] -= 1
        
    else:
        add_shape(grid, shapes[shape_index], pos)
        shape_index = (1 + shape_index) % num_shapes
        maximum = max(get_max(shapes[shape_index], pos), maximum) 
        pos = [2, maximum + 4]
        num_rocks += 1
        
print(maximum)