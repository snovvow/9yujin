from sys import setrecursionlimit
setrecursionlimit(100000)

N = int(input())
graph = []
dp = [[-1] * N for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
    graph.append(list(map(int, input().split())))

def dfs(i,j):
    if dp[i][j] < 0:
        dp[i][j] = 0

        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            if 0 <= x < N and 0 <= y < N and graph[i][j] < graph[y][x]:
                dp[i][j] = max(dp[i][j], dfs(y,x))
        dp[i][j] += 1
    
    return dp[i][j]
    
ans = 0

for i in range(N):
    for j in range(N):
        ans = max(ans, dfs(i, j))

print(ans)