import heapq
import sys
INF = int(1e9)

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

def dijkstra(start):
    distance = [INF] * (N+1)
    queue = []
    # (dist, now)
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue: #큐가 비어있지 않다면
        # 가장 가까운 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(queue)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist :
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드 거치는게 더 빠른 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    return distance



for _ in range(M):
    start, end, t = map(int, sys.stdin.readline().split())
    graph[start].append((end, t))

ans = 0
for i in range(1, N+1):
    go = dijkstra(i)[X]
    back = dijkstra(X)[i]
    ans = max(ans, go + back)

print(ans)