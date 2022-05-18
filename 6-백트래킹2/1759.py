from itertools import combinations

l,c = map(int, input().split())
arr = sorted(list(input().split()))

comb = list(combinations(arr, l))
sorted_comb = []
for i in range(len(comb)):
    list_comb = list(comb[i])
    sorted_comb.append(list_comb)

for i in sorted_comb:
    count = 0
    for ch in i:
        if ch in ['a','e','i','o','u']:
            count += 1
    if count > 0 and 2 < l-count:
        print(''.join(i))
    