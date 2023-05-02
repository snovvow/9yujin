from collections import deque
import sys

def bfs(i,j):
    q = deque()
    q.append([i,j])
    temp = []
    temp.append([i,j])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
                if L <= abs(graph[nx][ny] - graph[x][y]) <= R :
                    visit[nx][ny] = 1
                    q.append([nx,ny])
                    temp.append([nx,ny])
    return temp



N, L, R = map(int, input().split())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = 0
graph = []

for _ in range(N):
    graph.append((list(map(int, sys.stdin.readline().rstrip().split()))))

while True:
    visit = [[0]* N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                visit[i][j] = 1
                union = bfs(i,j)
                print(union)
                if len(union) > 1:
                    flag = 1
                    new_population = sum([graph[x][y] for x,y in union]) // len(union)
                    for x,y in union:
                        graph[x][y] = new_population
    if flag == 1:
        break
    result += 1
    

print(result)
