def find_word(input, word):
    rows = len(input)
    cols = len(input[0])
    count = 0

    # Directions: (row_offset, col_offset)
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Down-Right
        (-1, -1), # Up-Left
        (1, -1),  # Down-Left
        (-1, 1)   # Up-Right
    ]

    def is_valid(x, y):
        # Check if coordinates are within grid bounds
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, direction):
        dx, dy = direction
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or input[nx][ny] != word[i]:
                return False
        return True

    # Search the grid
    for x in range(rows):
        for y in range(cols):
            for direction in directions:
                if search_from(x, y, direction):
                    count += 1

    return count

f = open("input.txt", "r")
lines = f.readlines()

# Convert the string into a list of lists
grid = [list(line.strip()) for line in lines]

word = "XMAS"
output = find_word(grid, word)
print(output)
