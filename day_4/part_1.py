class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.pop()
    

contents = [i for i in open("day_4/input.txt", "r").read().split("\n\n")]
cranes = contents[0]
instructions = contents[1]
instructions = instructions.split("\n")
cranes = cranes.split("\n")
cranes.pop(-1)


stacks = []
for i in range(1, len(cranes[0]), 4):
    pile = []
    stacks.append(pile)
for pile in cranes:
    for i in range(1, len(pile), 4):
        if pile[i] != " ":
            stacks[(i - 1) // 4].append(pile[i])

for i in range(len(stacks)):
    stacks[i].reverse()

for stack in stacks:
    print(stack)

for i in range(len(instructions)):
    instructions[i] = instructions[i].replace("move", "")
    instructions[i] = instructions[i].replace("from", "")
    instructions[i] = instructions[i].replace("to", "")
    instructions[i] = instructions[i].split()

for instruction in instructions:
    """for _ in range(int(instruction[0])):
        item = stacks[int(instruction[1]) - 1].pop()
        stacks[int(instruction[2]) - 1].append(item)
    """
    items = stacks[int(instruction[1]) - 1][-1 * int(instruction[0]):]
    stacks[int(instruction[2]) - 1] = stacks[int(instruction[2]) - 1] + items
    del stacks[int(instruction[1]) - 1][-1 * int(instruction[0]):]
    
    
    
print("Happened")
for stack in stacks:       
    print(stack)
    
    