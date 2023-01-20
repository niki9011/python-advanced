def fill_the_box(*args):
    box = args[0] * args[1] * args[2]
    result = 0

    while True:
        for x in args[3:]:
            if x == "Finish":
                break
            else:
                result += x

        if box > result:
            return f"There is free space in the box. You could put {box - result} more cubes."
        else:
            return f"No more free space! You have {result - box} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))

