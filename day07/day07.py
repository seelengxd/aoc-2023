import sys
from collections import Counter
data = [line.split() for line in sys.stdin]

order = "AKQT98765432J"[::-1]
big = 99


def key(cards):
    c = Counter(cards)

    five_of_kind = False
    four_of_kind = False
    full_house = False
    three_of_kind = False
    two_pair = False
    one_pair = False
    high_card = False

    skip = True
    if "J" in c:
        if c["J"] == 1:
            # 2 2
            if list(c.values()).count(2) == 2:
                full_house = True
            # 1 1 1 1
            elif list(c.values()).count(1) == 5:
                one_pair = True
            # 1 3
            elif 3 in c.values():
                four_of_kind = True
            # 4
            elif 4 in c.values():
                five_of_kind = True
                # 1 2 1
            else:
                three_of_kind = True
        elif c["J"] == 2:
            # 3
            if 3 in c.values():
                five_of_kind = True
            # 2 1
            elif list(c.values()).count(2) == 2:
                four_of_kind = True
            # 1 1 1
            else:
                three_of_kind = True
        elif c["J"] == 3:
            if 2 in c.values():
                five_of_kind = True
            else:
                four_of_kind = True
        elif c["J"] >= 4:
            five_of_kind = True
        else:
            skip = False
    else:
        skip = False

    v = list(c.values())
    first = order.index(cards[0])

    if not skip:
        five_of_kind = 5 in v
        four_of_kind = 4 in v
        full_house = full_house or (3 in v and 2 in v)
        three_of_kind = 3 in v
        two_pair = v.count(2) == 2
        one_pair = 2 in v
        high_card = len(set(cards)) == 5

    result = [five_of_kind, four_of_kind, full_house,
              three_of_kind, two_pair, one_pair, high_card]

    return (-result.index(True), first, order.index(cards[1]), order.index(cards[2]), order.index(cards[3]), order.index(cards[4]))


data.sort(key=lambda i: key(i[0]))
ans = 0
for index, (card, num) in enumerate(data, 1):
    ans += int(num) * index
print(ans)
