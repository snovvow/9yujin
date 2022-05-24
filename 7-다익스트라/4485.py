import heapq
import sys

def dijkstra(init, x,y):
    queue = []
    # (dist, now_x, now_y)
    heapq.heappush(queue, (init, x,y))
    distance[x][y] = init

    while queue: # 큐가 비어있지 않다면
            # 가장 가까운 노드에 대한 정보 꺼내기
            dist, x, y = heapq.heappop(queue)
            # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            if distance[x][y] < dist :
                continue
            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or  ny >= n:
                    continue
                new_cost = dist + graph[nx][ny]
                # 현재 노드 거치는게 더 빠른 경우
                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heapq.heappush(queue, (new_cost, nx, ny))

# -------------------------------------------------------- #

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]  
INF = int(1e9)
count = 0

while(1):
    n = int(input())
    graph = []

    # 모든 간선 정볼 입력
    for _ in range(n):
        row  = list(map(int, sys.stdin.readline().split()))
        # a번 노드에서 b번 노드로 가는 거리가 c
        graph.append(row)

    distance = [[INF] * n for _ in range(n)]
    if not n:
        break

    dijkstra(graph[0][0],0,0)
    count += 1
    print("Problem {0}: {1}".format(count, distance[n-1][n-1]))