class File:
    def __init__(self, name):
        self.name = name
        parent = None
        self.size = 0
        self.children = []
        
    def get_total(self):
        total = self.size
        for child in self.children:
            total += child.get_total()
        self.size = total
        return total
    
    def get_under(self, x):
        total = 0
        for child in self.children:
            total += child.get_under(x)
        if self.size < x:
            total += self.size
        return total
    
    def add(self, child):
        self.children.append(child)
        
    def __str__(self):
        out = self.name + " " + str(self.size) + "\n"
        for child in self.children:
            out += str(child)
        return out
    
    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
                

contents = [line for line in open("day_7/input.txt").read().split("\n")]
file = File("/")
rootFile = file

for line in contents[1:]:
    line = line.split(" ")
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                file = file.parent
            else:
                file = file.get_child(line[2])
    elif line[0] == "dir":
        newFile = File(line[1])
        newFile.parent = file
        file.add(newFile)
    else:
        file.size += int(line[0])
        
rootFile.get_total()
print(rootFile)
print(rootFile.get_under(100000))
    
        