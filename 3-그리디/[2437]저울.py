# https://seongonion.tistory.com/127

import sys

n = int(input())
arr= list(map(int, sys.stdin.readline().split()))
arr.sort()

result = 0
for i in range(n):
    if result + 1 >= arr[i]:
        result += arr[i]
    else:
        break

print(result + 1)