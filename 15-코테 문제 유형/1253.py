from itertools import combinations
import copy
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))


def sol(arr, target):
    comb = list(combinations(arr, 2))
    sumSet = set()
    for i in comb:
        sumSet.add(i[0]+i[1])
    if target in sumSet:
        return 1
    else:
        return 0

ans = 0
for i in range(len(A)):
    tempA = copy.deepcopy(A)
    target = tempA.pop(i)

    if sol(tempA,target) == 1:
        ans += 1

print(ans)

    