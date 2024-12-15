import re

def sum_valid_muls(input):
    # Regular expression to find valid `mul(a,b)` instructions
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input)
    
    total = sum(int(a)*int(b) for a,b in matches)
    
    return total

# Example memory input
with  open("input.txt","r") as file:
    str = file.read()

file.close()

# Compute the sum of valid mul instructions
output = sum_valid_muls(str)

print(output)