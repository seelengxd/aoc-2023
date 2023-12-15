import sys

data = [list(map(int, line.strip().split())) for line in sys.stdin]


def calculate_diff_row(row):
    return [row[i + 1] - row[i] for i in range(len(row) - 1)]


def calculate_diff(data):
    result = []
    for row in data:
        result.append(calculate_diff_row(row))
    return result


def calculate(data, reverse=False):
    ans = 0
    for row in data:
        temp = [row[::]]
        while True:
            if all(i == 0 for i in temp[-1]):
                break
            temp.append(calculate_diff_row(temp[-1]))
        if reverse:
            temp = [row[::-1] for row in temp]
        n = len(temp)
        temp[n - 1].append(0)

        for i in range(n - 2, -1, -1):
            temp[i].append(temp[i][-1] - temp[i + 1][-1]
                           if reverse else temp[i][-1] + temp[i + 1][-1])
        ans += temp[0][-1]
    return ans


print("Part 1:", calculate(data))
print("Part 2:", calculate(data, reverse=True))
