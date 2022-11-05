INF = 999999999
d = [-1,0,1]

N, M = map(int,input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

def Dfs(r,c, previousD):
    if r == N:
        return 0
    temp = INF
    for direction in d:
        # 이전이랑 똑같은 방향
        if direction == previousD:
            continue
        # 범위 벗어나는 경우
        if c + direction < 0 or c + direction >= M:
            continue
        temp = min(temp, Dfs(r+1, c + direction, direction)+graph[r][c])
    return temp

ans = INF
for i in range(M):
    ans = min(ans, Dfs(0, i ,2))

print(ans)