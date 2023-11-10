def add(value1, value2):
    return value1 + value2

def multiply(value1, value2):
    return value1 * value2

def square(value, value2):
    return value ** 2

class Monkey:
    def __init__(self):
        self.modulo = None
        self.total = 0
        self.values = []
        self.dividor = None
        self.throwers = []
        self.move = []
        
    def set_dividor(self, dividor):
        self.dividor = dividor
        
    def set_values(self, values):
        self.values = [int(i) for i in values.split(", ")]
        
    def add_thrower(self, monkey):
        self.throwers.append(monkey)
        
    def set_operation(self, operation, number):
        if number == "old":
            self.move.append(square)
            self.move.append(" ")
            return
            
        if operation == "+":
            self.move.append(add)
        elif operation == "*":
            self.move.append(multiply)
        
        self.move.append(int(number))
        
        
    def update(self):
        while self.values != []:
            item = self.values.pop(0)
            new = self.move[0](item, self.move[1]) % self.modulo
            if new % self.dividor == 0:
                self.throwers[0].get(new)
            else:
                self.throwers[1].get(new)
            self.total += 1
            
    def get(self, item):
        self.values.append(item)
        
    def __str__(self):
        return str(self.total)
        
        
input_file = open("day_11/input.txt", "r")
contents = input_file.read().split("\n\n")
input_file.close()

monkeys = []
for i in range(len(contents)):
    monkeys.append(Monkey())
    contents[i] = contents[i].split("\n")

modulo = 1
for i in range(len(contents)):
    monkeys[i].set_values(contents[i][1].split(": ")[1])
    contents[i][2] = contents[i][2].strip().split(" ")
    monkeys[i].set_operation(contents[i][2][4], contents[i][2][5])
    monkeys[i].set_dividor(int(contents[i][3].strip().split()[3]))
    modulo *= monkeys[i].dividor
    monkeys[i].add_thrower(monkeys[int(contents[i][4].strip().split()[5])])
    monkeys[i].add_thrower(monkeys[int(contents[i][5].strip().split()[5])])

for monkey in monkeys:
    monkey.modulo = modulo

for i in range(10000):
    for monkey in monkeys:
        monkey.update()
        
for monkey in monkeys:
    print(monkey.total)
    
num_maxes = 2
max = [0] * num_maxes
for monkey in monkeys:
    if monkey.total > max[0]:
        max[1] = max[0]
        max[0] = monkey.total
    elif monkey.total > max[1]:
        max[1] = monkey.total
        
print(max[0] * max[1])


            
            
    
    