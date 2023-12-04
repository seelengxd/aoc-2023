import re
part1 = 0
win_per_card = {}
count_per_card = {}
with open("day04.in") as f:
    for index, line in enumerate(f, 1):
        data = line.split(":")[1]
        win, have = map(lambda l: list(
            map(int, re.split(" +", l.strip()))), data.split("|"))
        count = len(set(win).intersection(set(have)))
        if count:
            part1 += 1 << (count - 1)
        win_per_card[index] = count

for i in range(1, len(win_per_card) + 1):
    count_per_card[i] = 1

for i in range(1, len(win_per_card) + 1):
    count = count_per_card[i]
    for w in range(1, win_per_card[i] + 1):
        count_per_card[i + w] += count

print(part1)
# part 2
print(sum(count_per_card.values()))
