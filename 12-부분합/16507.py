import sys

R,C,A = map(int, input().split())

arr = []
for _ in range(R):
    arr.append(list(map(int, sys.stdin.readline().split())))

d = [[0]*(C+1) for i in range(R+1)]

for r in range(1, R+1):
    for c in range(1, C+1):
        d[r][c] = d[r-1][c] + d[r][c-1] + arr[r-1][c-1] - d[r-1][c-1]

for i in range(A):
    r1,c1, r2, c2 = map(int, input().split())
    ans = d[r2][c2] - d[r1-1][c2] - d[r2][c1-1] + d[r1-1][c1-1]
    print(ans // ((r2 -r1 + 1) * (c2 - c1 + 1)))