import sys
import re

data = [line for line in sys.stdin]

seeds = list(map(int, data[0].split(": ")[1].strip().split()))
maps = "".join(data[2:]).strip().split("\n\n")


def intersection(a, b, c, d):
    # [a, b] [c, d]
    if b < c or d < a:
        return None

    # let a <= c for calculating intersection
    if a > c:
        a, b, c, d = c, d, a, b

    return [c, min(b, d)]


def parse_map(s):

    source_name, dest_name = re.findall("(.+)-to-(.+) map", s)[0]
    data = list(map(lambda i: i.split("\n"), s.split(":\n")[1:]))[0]
    data = list(map(lambda line: list(map(int, line.split())), data))

    def mapper(i):
        for dest, source, r in data:
            if 0 <= i - source < r:
                return dest + (i - source)
        return i

    def mapper_range(s, e):
        # given s, e, return [(s, e)] of ranges this can correspond to
        ranges = []
        stack = [(s, s + e - 1)]
        while len(stack):
            s1, e1 = stack.pop()
            for dest, source, r in data:
                # [source, source + r], [s, e] intersection
                intersect = intersection(source, source + r - 1, s1, e1)
                if intersect:
                    int_s, int_e = intersect
                    ranges.append((dest + int_s - source, int_e - int_s + 1))
                    if int_s > s1:
                        stack.append((s1, int_s - 1))
                    if int_e < e1:
                        stack.append((int_e + 1, e1))
                    break
            else:
                ranges.append((s1, e1 - s1 + 1))
        return ranges

    return source_name, dest_name, mapper, mapper_range


maps = list(map(parse_map, maps))
locations = []
for seed in seeds:
    location = seed
    for _, _, mapper, _ in maps:
        location = mapper(location)
    locations.append(location)
print("part 1", min(locations))


iter_seeds = iter(seeds)
ranges = [(s, e) for s, e in zip(iter_seeds, iter_seeds)]
for _, _, _, mapper_range in maps:
    next_ranges = []
    for r in ranges:
        next_ranges += mapper_range(*r)
    ranges = next_ranges

print("part 2", min([i[0] for i in ranges]))
