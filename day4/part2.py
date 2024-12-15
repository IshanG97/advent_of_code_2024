def find_word(input, word):
    center_char = word[len(word)//2]
    reverse_word = word[::-1]
    rows = len(input)
    cols = len(input[0])
    count = 0

        # Check if a word exists diagonally
    def check_diagonal(x, y, dx, dy, word_to_check):
        for i in range(len(word_to_check)):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols) or input[nx][ny] != word_to_check[i]:
                return False
        return True

    # Check for an X-MAS pattern centered at (x, y)
    def is_xmas_center(x, y):
        # Ensure the center matches the middle character of the word
        if input[x][y] != center_char:
            return False

        # Check both diagonals for valid "MAS" or "SAM"
        top_left_to_bottom_right = (
            check_diagonal(x - 1, y - 1, 1, 1, word) or
            check_diagonal(x - 1, y - 1, 1, 1, reverse_word)
        )
        bottom_left_to_top_right = (
            check_diagonal(x + 1, y - 1, -1, 1, word) or
            check_diagonal(x + 1, y - 1, -1, 1, reverse_word)
        )

        # Both diagonals must form the X pattern
        return top_left_to_bottom_right and bottom_left_to_top_right

        # Iterate through the grid
    for x in range(1, rows - 1):  # Avoid edges where an X pattern can't fit
        for y in range(1, cols - 1):
            if is_xmas_center(x, y):
                count += 1

    return count

f = open("input.txt", "r")
lines = f.readlines()

# Convert the string into a list of lists
grid = [list(line.strip()) for line in lines]

word = "MAS"
output = find_word(grid, word)
print(output)
