import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

def main_bfs(heightmap, start):
    visited = initialize_visited(start)
    queue = [(start, 0)]
    val = None
    while val == None and queue != []:
        val = bfs(heightmap, visited, queue)
    """for y in range(len(heightmap)):
        for x in range(len(heightmap[0])):
            print(int(visited[x][y]), end = "")
        print()"""
    return val
        
        
def bfs(heightmap, visited, queue):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    curr_pos, depth = queue.pop(0)
    curr_letter = heightmap[curr_pos[1]][curr_pos[0]]
    directions = [np.array([-1, 0]), np.array([0, -1]), np.array([1, 0]), np.array([0, 1])]
    for direction in directions:
        new_pos = curr_pos + direction
        if 0 > new_pos[0] or new_pos[0] >= len(heightmap[0]) or 0 > new_pos[1] or new_pos[1] >= len(heightmap):
            continue 
        new_letter = heightmap[new_pos[1]][new_pos[0]]
        
        if visited[new_pos[0]][new_pos[1]] != 0:
            continue
        
        if new_letter == 'E':
            if curr_letter == "z" or curr_letter == "y":
                print(depth + 1)
                return depth + 1
            else:
                continue
        
        if curr_letter == "S":
            curr_letter = "a"
        
        if letters.index(new_letter) <= letters.index(curr_letter) + 1:
            queue.append((new_pos, depth + 1))
            visited[new_pos[0]][new_pos[1]] = 1
            
       
def initialize_visited(start):
    visited = np.zeros((len(heightmap[0]), len(heightmap)))
    visited[start[0]][start[1]] = 1 
    return visited
        
starts = []
heightmap = [i for i in open("day_12/input.txt", "r").read().split("\n")]
for y in range(len(heightmap)):
    for x in range(len(heightmap[0])):
        if heightmap[y][x] == "S":
            starts.append(np.array([x, y]))
            heightmap[y] = heightmap[y][:x] + "a" + heightmap[y][x + 1:]
        if heightmap[y][x] == "a":
            starts.append(np.array([x, y]))

minimum = main_bfs(heightmap, starts[0])
for start in starts[1:]:
    min = main_bfs(heightmap, start)
    if min == None:
        continue
    if min < minimum:
        minimum = min
print(minimum)

        
        
    
    
    
    
    
    
    