M = int(input())
stock = list(map(int, input().split()))
DAY = 14


def calcAsset(args):
    return args[0] + args[1] * stock[13]


def BNP():
    money = M
    has = 0

    for v in stock:
        count = money // v

        has += count
        money -= count * v
    return money, has


def TIMING():
    money = M
    has = 0
    rise = 0
    fall = 0

    for i, v in enumerate(stock):
        if i > 0:
            if stock[i - 1] > stock[i]:
                fall += 1
                rise = 0
            elif stock[i - 1] < stock[i]:
                fall = 0
                rise += 1
            elif stock[i - 1] == stock[i]:
                fall = 0
                rise = 0

        if fall >= 3:
            count = money // v
            has += count
            money -= count * v
        elif rise >= 3:
            money += v * has
            has = 0

    return money, has


bnp = calcAsset(BNP())
timing = calcAsset(TIMING())

if bnp > timing:
    print("BNP")
elif bnp < timing:
    print("TIMING")
else:
    print("SAMESAME")
