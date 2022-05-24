import heapq
import sys
INF = int(1e9)

v, e, p = map(int, input().split())
graph = [[]for _ in range(v+1)]


# 간선정보 입력
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

# 다익스트라
def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start)) # (dist, now)
    distance = [INF] * (v+1)
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    return distance


""" 출발점인 1번 노드부터 V까지 가는 최단경로의 길이가 1 -> P, P -> V의 최단거리 합과 같다면 
P를 거쳐서 지나가도 최단거리라는 뜻이므로 건우를 구할 수 있습니다. 같지 않은 경우 건우는 버려집니다. """
if dijkstra(1)[v] == dijkstra(1)[p] + dijkstra(p)[v]:
    print("SAVE HIM")
else:
    print("GOOD BYE")