# S is F for my input

import sys
from collections import deque

pipe_directions = {
    "|": ["N", "S"],
    "-": ["E", "W"],
    "L": ["N", "E"],
    "J": ["N", "W"],
    "7": ["S", "W"],
    "F": ["S", "E"],
}

opposite_direction = {
    "N": "S",
    "S": "N",
    "E": "W",
    "W": "E"
}

direction_coords = {
    "N": [-1, 0],
    "S": [1, 0],
    "E": [0, 1],
    "W": [0, -1]
}


def get_other_direction(pipe_type, direction):
    return pipe_directions[pipe_type][not pipe_directions[pipe_type].index(direction)]


def travel(from_direction, x, y, pipe_type):
    """Travel to `pipe type` from `from_direction`, returns next coordinates"""
    assert from_direction in pipe_directions[pipe_type]
    other_direction = get_other_direction(pipe_type, from_direction)
    dx, dy = direction_coords[other_direction]
    return x + dx, y + dy, other_direction


start_pipe = "F"

data = [list(line.strip()) for line in sys.stdin]
m = len(data)
n = len(data[0])
sx, sy = None, None
for i in range(m):
    for j in range(n):
        if data[i][j] == "S":
            sx = i
            sy = j
            data[i][j] = start_pipe

q = deque()
first = True
for direction in pipe_directions[start_pipe]:
    q.append((0, sx, sy, direction))

visited = set()
ans = 0
while q:
    distance, x, y, from_dir = q.popleft()
    # print(x, y)
    if (x, y) in visited:
        continue
    if first:
        first = False
    else:
        visited.add((x, y))
    ans = max(ans, distance)
    next_x, next_y, out_dir = travel(from_dir, x, y, data[x][y])
    q.append((distance + 1, next_x, next_y, opposite_direction[out_dir]))
print(ans)


def convert_junk(data, visited):
    result = []
    for i in range(len(data)):
        new_row = []
        for j in range(len(data[0])):
            if (i, j) not in visited:
                new_row.append(".")
            else:
                new_row.append(data[i][j])
        result.append(new_row)
    return result


converted = convert_junk(data, visited)


def green_print(c):
    print('\x1b[6;30;42m' + c + '\x1b[0m', end="")


def yellow_print(c):
    print('\x1b[6;30;43m' + c + '\x1b[0m', end="")


def map_expander(data):
    m = len(data)
    n = len(data[0])
    mapper = {
        "|": [
            ["X", "|", "X"],
            ["X", "|", "X"],
            ["X", "|", "X"]],
        "-": [
            ["X", "X", "X"],
            ["-", "-", "-"],
            ["X", "X", "X"]],
        "L": [
            ["X", "|", "X"],
            ["X", "L", "-"],
            ["X", "X", "X"]],
        "J": [
            ["X", "|", "X"],
            ["-", "J", "X"],
            ["X", "X", "X"]],
        "7": [
            ["X", "X", "X"],
            ["-", "7", "X"],
            ["X", "|", "X"]],
        "F": [
            ["X", "X", "X"],
            ["X", "F", "-"],
            ["X", "|", "X"]],
        ".": [
            ["X", "X", "X"],
            ["X", ".", "X"],
            ["X", "X", "X"]]
    }
    new_map = [[None] * (n * 3) for _ in range(m * 3)]
    for i in range(m):
        for j in range(n):
            pipe = data[i][j]
            pipe_expanded = mapper[pipe]
            start_x = i * 3
            start_y = j * 3
            for a in range(3):
                for b in range(3):
                    new_map[start_x + a][start_y + b] = pipe_expanded[a][b]
    return new_map


expanded = map_expander(converted)
outside = []
visited = set()
total_dots = sum([row.count(".") for row in converted])
for i in range(m * 3):
    outside.append((i, 0))
    outside.append((i, n * 3 - 1))

for j in range(n * 3):
    outside.append((0, j))
    outside.append((m * 3 - 1, j))

while outside:
    x, y = outside.pop()
    # outside range or visited, continue
    if x < 0 or x >= (m * 3) or y < 0 or y >= (n * 3) or (x, y) in visited:
        continue
    if expanded[x][y] not in ["X", "."]:
        continue

    if expanded[x][y] == ".":
        total_dots -= 1
    visited.add((x, y))
    outside += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
print(total_dots)


def printer():
    for row in expanded:
        print("".join(row))

    for i in range(m):
        for j in range(n):
            if (i, j) in visited:
                green_print(data[i][j])
            elif data[i][j] == ".":
                yellow_print(data[i][j])
            else:
                print(data[i][j], end="")
        print()

    for i in range(m * 3):
        for j in range(n * 3):
            if (i, j) in visited:
                green_print(expanded[i][j])
            elif expanded[i][j] == ".":
                yellow_print(expanded[i][j])
            else:
                print(expanded[i][j], end="")
        print()
