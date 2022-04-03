def dfs(graph, v, visited):
    visited[v] = True
    result.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i ,visited)

n = int(input())
m = int(input())

#graph[0]은 비운다. 노드번호와 인덱스를 맞추기위해
graph =[[] for _ in range(n+1)]
result=[]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)


dfs(graph, 1, visited)
print(len(result)-1)

# ----- 이전에 풀었던 BFS 방식 코드입니다.

""" from collections import deque
n = int(input())
m = int(input())

graph = [[]  for _ in range(n+1)]

for i in range(m): #인접 리스트 방식으로 그래프 만들기
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited = [False] * (n+1)


def Dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ") #시작점 방문 처리
    for i in graph[v]:  # graph[v] : v와 연결된 다른 노드들
        if not visited[i]:
            Dfs(graph,i,visited)

def Bfs(graph, start, visited):
    count = 0
    queue = deque([start]) #처음에 시작점 큐에 넣고
    visited[start] = True #방문처리
    while queue:
        v = queue.popleft() #큐에서 하나 뽑아서
        #print(v, end=" ") #프린트
        count += 1
        for i in graph[v]: # graph[v] : v와 연결된 다른 노드들
            if not visited[i]:
                queue.append(i) #큐에 박아
                visited[i] = True
    return count
result = Bfs(graph, 1, visited)
print(result -1) """