rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input().split()

    if command[0] == "END":
        break

    row, col, value = [int(x) for x in command[1:]]

    if row >= 0 and row <= rows - 1 and col >= 0 and col <= rows - 1:
        if command[0] == "Add":
            matrix[row][col] += value

        elif command[0] == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

[print(*x) for x in matrix]
