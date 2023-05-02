from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))

result = []
for i in range(1, len(arr)+1):
  result = result + list(combinations(arr,i))  

count = 0
for i in result:
  sum = 0
  for j in i:
    sum += j
  if sum == S:
    count += 1
print(count)