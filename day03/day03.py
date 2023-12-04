import string

with open("day03.in") as f:
    data = [line.strip() for line in f.readlines()]

m = len(data)
n = len(data[0])

used = [[0] * n for _ in range(m)]


def reset_used():
    global used
    used = [[0] * n for _ in range(m)]


def read(i, j):
    return data[i][j] if 0 <= i < m and 0 <= j < n else "."


def is_symbol(c):
    return c not in string.digits + "."


def mark_and_return_number(i, j):
    to_add = [data[i][j]]
    used[i][j] = 1
    for k in range(j - 1, -1, -1):
        if data[i][k].isdigit():
            used[i][k] = 1
            to_add.insert(0, data[i][k])
        else:
            break
    for k in range(j + 1, n):
        if data[i][k].isdigit():
            used[i][k] = 1
            to_add.append(data[i][k])
        else:
            break
    return int("".join(to_add))


part1 = 0

for i in range(m):
    for j in range(n):
        if not used[i][j] and data[i][j].isdigit() and any([is_symbol(read(x, y)) for x in range(i - 1, i + 2) for y in range(j - 1, j + 2)]):
            part1 += mark_and_return_number(i, j)


print(part1)

part2 = 0
for i in range(m):
    for j in range(n):
        if data[i][j] == "*":
            reset_used()
            numbers = []
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if not used[x][y] and data[x][y].isdigit():
                        numbers.append(mark_and_return_number(x, y))
            if len(numbers) == 2:
                part2 += numbers[0] * numbers[1]

print(part2)
