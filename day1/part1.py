with open('input.txt', 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]


left, right = [],[]

for pair in lines:
    l, r = pair.split() #split on  whitespace
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

output = sum(abs(l-r) for l, r in zip(left, right))

print(output)