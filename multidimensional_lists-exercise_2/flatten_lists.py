rows = input().split("|")

matrix = []

for n in range(len(rows) - 1, -1, -1):
    matrix.extend(rows[n].strip().split())
print(" ".join(matrix))

#     if rows:
#         for z in rows.pop().split():
#             if z == " ":
#                 continue
#             else:
#                 matrix.append(z)
# print(" ".join(matrix))
