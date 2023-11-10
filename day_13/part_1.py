from functools import cmp_to_key

def compare(left, right):
    if left == right:
        return None
    
    if type(left) == int:
        if type(right) == int:
            return left < right
        else:
            return compare([left], right)
            
    if type(right) == int:
        return compare(left, [right])
    
    for i in range(min(len(left), len(right))):  
        temp = compare(left[i], right[i])
        if temp == None:
            continue
        
        return temp
    
    return len(left) <= len(right)


input_file = open("day_13/test.txt", "r")
contents = input_file.read()
contents = contents.replace("10", "#")
contents = contents.split("\n\n")
input_file.close()

lists = []
for pair in contents:
    pair = pair.split("\n")
    for item in pair:
        first = []
        stack = []
        lists.append(first)
        stack.append(first)
        for character in item[1:]:
            if character == ",":
                pass
            elif character == "[":
                new_list = []
                stack[-1].append(new_list)
                stack.append(new_list)
            elif character == "]":
                stack.pop()
            elif character == "#":
                stack[-1].append(10)
            else:
                stack[-1].append(int(character))

total = 0
truth = []
for i in range(0, len(lists), 2):
    total += compare(lists[i], lists[i + 1]) * (i // 2 + 1)
    truth.append(compare(lists[i], lists[i + 1]) * (1))
    
total = 0
for i in range(len(truth)):
    total += (i + 1) * truth[i]
print(truth)
print(total)

temp = [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1]



for list in lists:
    print(list)

            
