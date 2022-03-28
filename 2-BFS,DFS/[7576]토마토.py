from ipaddress import collapse_addresses


#bfs : deque 사용
from collections import deque

def bfs():
    while queue:
        # 익은토마토 하나 꺼내서 탐색시작
        x,y = queue.popleft()
        
        # 네가지 방향
        for i in range(4):
            # 다음 좌표
            nx, ny = dx[i] + x, dy[i] + y
            if -1 < nx < m and -1 < ny < n and graph[nx][ny] == 0:
                # 안익은 토마토가 있으면 큐에 넣고, +1
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx,ny])


n, m = map(int, input().split())
graph = []
queue =deque([])

dx=[-1,1,0,0]
dy=[0,0,-1,1]


for i in range(m):
    graph.append(list(map(int, input().split())))

    # 익은 토마토는 큐에 저장
    for j in range(n):
        if graph[i][j] == 1:
            queue.append([i,j])

bfs()

maxValue = 0
for i in graph:
    for j in i:
        # 익지 않은 토마토가 있을떄
        if j == 0:
            print(-1)
            exit()
    maxValue = max(maxValue, max(i))
print(maxValue-1)