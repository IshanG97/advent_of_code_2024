import re

def sum_enabled_muls(input):
    # Regular expressions for instructions
    mul_pattern = r"mul\((\d+),(\d+)\)"  # Matches `mul(a,b)`
    do_pattern = r"do\(\)"               # Matches `do()`
    dont_pattern = r"don't\(\)"          # Matches `don't()`

    # Initialize state
    is_enabled = True
    total = 0

    # Scan through the memory sequentially
    position = 0
    while position < len(input):
        # Check for `do()`
        do_match = re.match(do_pattern, input[position:])
        if do_match:
            is_enabled = True
            position += do_match.end()
            continue

        # Check for `don't()`
        dont_match = re.match(dont_pattern, input[position:])
        if dont_match:
            is_enabled = False
            position += dont_match.end()
            continue

        # Check for `mul(a,b)`
        mul_match = re.match(mul_pattern, input[position:])
        if mul_match:
            if is_enabled:
                a,b = map(int, mul_match.groups())
                total += a * b
            position += mul_match.end()
            continue

        # Move to the next character if no match
        position += 1

    return total

with  open("input.txt","r") as file:
    str = file.read()

file.close()

output = sum_enabled_muls(str)

print(output)
