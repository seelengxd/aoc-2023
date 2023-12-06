import sys
import re
import math

time, distance = map(lambda line: [int(i)
                     for i in re.split(" +", line)[1:]], sys.stdin)

ans = 1
for t, d in zip(time, distance):
    curr = 0
    for i in range(t):
        if i * (t - i) >= d:
            curr += 1
    ans *= curr
print(ans)

time = int("".join(map(str, time)))
distance = int("".join(map(str, distance)))


def solution(time, distance):
    a = 1
    b = -time
    c = distance
    disc = b * b - 4 * a * c
    left = (-b - disc ** 0.5) / (2 * a)
    right = (-b + disc ** 0.5) / 2 * a
    if left > time:
        return 0
    return math.floor(right) - math.ceil(left) + 1


print(solution(time, distance))
