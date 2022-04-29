# https://seongonion.tistory.com/127

""" import sys

n = int(input())
arr= list(map(int, sys.stdin.readline().split()))
arr.sort()

result = 0
for i in range(n):
    if result + 1 >= arr[i]:
        result += arr[i]
    else:
        break

print(result + 1) """

import sys
input = sys.stdin.readline

def find(weight,N):
  num = 1
  for x in range(1,N):
    if weight[x]-num >= 1:
      num += 1
      break
    num += weight[x]
  return num

N = int(input())
weight = list(map(int, input().split()))
weight.sort() # [1,1,2,3,6,7,30]

ans = 1
if weight[0] == 1:
  ans = find(weight,N)

print(ans)