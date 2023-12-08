import sys
import re
import itertools
from math import lcm

data = [line.strip() for line in sys.stdin]
directions = data[0]

m = {}

for line in data[2:]:
    n, l, r = re.findall("(.+) = \((.+), (.+)\)", line)[0]
    m[n] = l, r


def part1():
    curr = "AAA"
    for index, d in enumerate(itertools.cycle(directions), 1):
        curr = m[curr][d == "R"]
        if curr == "ZZZ":
            print(index)
            break


def helper(curr):
    curr = curr
    for index, d in enumerate(itertools.cycle(directions), 1):
        curr = m[curr][d == "R"]
        if curr.endswith("Z"):
            return index

# part1()


def part2():
    # for each node, calculate steps to reach z, and node after one entire route cycle.
    memo = {}
    n = len(directions)
    for node in m:
        curr = node
        z = []
        if curr.endswith("Z"):
            z.append(0)
        for index, d in enumerate(directions, 1):
            curr = m[curr][d == "R"]
            if curr.endswith("Z"):
                z.append(index)
        if curr.endswith("Z"):
            z.append(n)
        memo[node] = set(z), curr
    ans = 0
    curr = [k for k in m if k.endswith("A")]
    processed = []
    for node in curr:
        old = 0
        a = []
        for _ in range(10):
            a.append(helper(node) + old)
            old = a[-1]
        # observation: they cycle to the same node, with same diff. start = diff
        diff = [a[i] - a[i - 1] for i in range(1, 10)]
        processed.append((a[0], diff[0]))

    ans = lcm(*[c[0] for c in processed])
    print(ans)


part2()
