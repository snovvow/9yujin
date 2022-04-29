import sys

n = int(input())
arr= []
dp = [0] * 1500001
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    if i + arr[i][0] <= n:
        dp[i + arr[i][0]] = max(dp[i] + arr[i][1], dp[i + arr[i][0]])
    dp[i+1] = max(dp[i+1], dp[i])

print(max(dp))