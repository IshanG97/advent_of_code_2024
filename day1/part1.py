# load your input as a list [],[]
with open("input.txt","r") as file:
    # make a list to capture the input
    lines = file.readlines()

# optional: memory cleanup
file.close()

# break down the rows in a list
lines = (line.strip() for line in lines)

left, right = [], []

for line in lines:
    l, r = line.split() # split on  whitespace
    left.append(int(l))
    right.append(int(r))

# arrange the input by ascending order
left.sort()
right.sort()

# delta between integers in both lists
output = sum(abs(a-b) for a,b in zip(left,right))

print(output)