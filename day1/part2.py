from collections import Counter

with open("input.txt", 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

left, right = [], []

for pair in lines:
    l,r = pair.split()
    left.append(int(l))
    right.append(int(r))

# Counter library method
right_count = Counter(right)

output = 0
for i in left:
    output += i * right_count.get(i,0)

'''
output = 0
# Nested loop method - less efficient, but does not use the Counter library
for i in range(len(left)):
    instances = 0
    for j in range(len(right)):
        if left[i]==right[j]:
            instances+=1
        else:
            continue
    
    output += (left[i]*instances)

'''

print(output)