import sys
data = [line.strip() for line in sys.stdin]
transposed = list(zip(*data))
rows_without_galaxy = [i for i in range(len(data)) if data[i].count("#") == 0]
cols_without_galaxy = [i for i in range(
    len(transposed)) if transposed[i].count("#") == 0]


def calculate(data, size=2):
    transposed = list(zip(*data))
    rows_without_galaxy = {i for i in range(
        len(data)) if data[i].count("#") == 0}
    cols_without_galaxy = {i for i in range(
        len(transposed)) if transposed[i].count("#") == 0}

    coords = []
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            if item == "#":
                coords.append((i, j))
    ans = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            a, b = coords[i]
            c, d = coords[j]
            curr = 0
            for row in rows_without_galaxy:
                if a < row < c or c < row < a:
                    curr += size - 1
            for col in cols_without_galaxy:
                if b < col < d or d < col < b:
                    curr += size - 1
            curr += abs(c - a) + abs(d - b)
            ans += curr
    return ans


print("Part 1:", calculate(data))
print("Part 2:", calculate(data, 1000000))
