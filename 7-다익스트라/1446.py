import heapq
import sys
INF = int(1e9)

n, d = map(int, (input().split()))
graph = [[] for _ in range(d+1)]
distance = [INF] * (d+1)

#모든 칸을 하나의 노드로
for i in range(d):
    graph[i].append((i+1, 1))

# 모든 간선 정볼 입력
for _ in range(n):
    a,b,c = map(int, sys.stdin.readline().split())
    # a번 노드에서 b번 노드로 가는 거리가 c
    if b <= d:
        graph[a].append((b,c))

def dijkstra(start):
    queue = []
    # (dist, now)
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue: # 큐가 비어있지 않다면
            # 가장 가까운 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(queue)
            # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            if distance[now] < dist :
                continue
            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for i in graph[now]:
                cost = dist + i[1]

                # 현재 노드 거치는게 더 빠른 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(queue, (cost, i[0]))

dijkstra(0)
print(distance[d])