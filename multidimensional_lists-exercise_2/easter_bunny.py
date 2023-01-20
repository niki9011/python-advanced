size = int(input())

matrix = []
bunny_row = 0
bunny_col = 0

directions = {
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c)
}

for _ in range(size):
    matrix.append(list(input().split()))

for row1 in range(size):
    for col1 in range(size):
        if matrix[row1][col1] == "B":
            bunny_row = row1
            bunny_col = col1

best_path = []
best_direct = ""
best_sum = float("-inf")

for direction in directions:
    the_sum = 0
    result = []
    row, col = directions[direction](bunny_row, bunny_col)

    while 0 <= row < size and 0 <= col < size and matrix[row][col] != "X":
        the_sum += int(matrix[row][col])
        result.append([row, col])
        row, col = directions[direction](row, col)

    if the_sum > best_sum:
        best_sum = the_sum
        best_direct = direction
        best_path = result

print(best_direct)
print(*best_path, sep="\n")
print(best_sum)