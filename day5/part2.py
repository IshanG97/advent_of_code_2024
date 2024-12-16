from collections import defaultdict, deque

# Read the input file
with open('input.txt', 'r') as file:
    string = file.read()

# Split the content into ordering rules and updates
sections = string.strip().split("\n\n")
ordering_rules = sections[0].splitlines()
updates = [list(map(int, line.split(','))) for line in sections[1].splitlines()]

# Function to validate if an update respects the ordering rules
def is_valid_update(update, dependencies):
    index_map = {page: i for i, page in enumerate(update)}
    for page, deps in dependencies.items():
        if page in index_map:
            for dep in deps:
                if dep in index_map and index_map[dep] > index_map[page]:
                    return False
    return True

# Function to correct the order of an update using topological sorting
def correct_order(update, dependencies):
    # Build the dependency graph for the given update
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for page in update:
        if page in dependencies:
            for dep in dependencies[page]:
                if dep in update:
                    graph[dep].append(page)
                    in_degree[page] += 1

    # Perform topological sorting
    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_update = []
    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return sorted_update

# Main function to fix incorrect updates
def fix_incorrect_updates(ordering_rules, updates):
    # Parse ordering rules into a dependency graph
    dependencies = defaultdict(list)
    for rule in ordering_rules:
        x, y = map(int, rule.split("|"))
        dependencies[y].append(x)

    # Identify invalid updates and correct them
    valid_updates = []
    corrected_updates = []
    for update in updates:
        if is_valid_update(update, dependencies):
            valid_updates.append(update)
        else:
            corrected_updates.append(correct_order(update, dependencies))

    # Calculate the middle pages for corrected updates
    corrected_middle_pages = [update[len(update) // 2] for update in corrected_updates]

    return sum(corrected_middle_pages)

# Using the functions to process the input data
output = fix_incorrect_updates(ordering_rules, updates)

# Output the results
print(output)
