def even_odd(*args):
    result = []
    command = args[-1]
    new = args[:-1]

    for x in new:
        if command == "even":
            if x % 2 == 0:
                result.append(x)
        elif command == "odd":
            if x % 2 != 0:
                result.append(x)

    return result

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
