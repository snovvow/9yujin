import sys

N,M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

d = [[0]*(M+1) for i in range(N+1)]

for r in range(1, N+1):
    for c in range(1, M+1):
        d[r][c] = d[r-1][c] + d[r][c-1] + arr[r-1][c-1] - d[r-1][c-1]

K = int(input())

for i in range(K):
    r1,c1, r2, c2 = map(int, sys.stdin.readline().split())
    ans = d[r2][c2] - d[r1-1][c2] - d[r2][c1-1] + d[r1-1][c1-1]
    print(ans)