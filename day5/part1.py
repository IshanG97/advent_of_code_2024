from collections import defaultdict

with open('input.txt', 'r') as file:
    string = file.read()

# Split the content into ordering rules and updates
sections = string.strip().split("\n\n")
ordering_rules = sections[0].splitlines()
updates = [list(map(int, line.split(','))) for line in sections[1].splitlines()]

# Parse ordering rules into a directed graph (dependency mapping)
dependencies = defaultdict(list)
for rule in ordering_rules:
    x, y = map(int, rule.split("|"))
    dependencies[y].append(x)

# Function to check if an update respects the ordering rules
def is_valid_update(update):
    index_map = {page: i for i, page in enumerate(update)}
    for page, deps in dependencies.items():
        if page in index_map:
            for dep in deps:
                if dep in index_map and index_map[dep] > index_map[page]:
                    return False
    return True

# Filter valid updates and find their middle page number
valid_updates = [update for update in updates if is_valid_update(update)]
middle_pages = [update[len(update) // 2] for update in valid_updates]

# Calculate the sum of the middle pages
output = sum(middle_pages)

print(output)