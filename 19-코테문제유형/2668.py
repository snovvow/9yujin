n = int(input())
#graph[0]은 비운다. 노드번호와 인덱스를 맞추기위해
graph =[[] for _ in range(n+1)]

def dfs(v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i,visited)


for i in range(1,n+1):
    a = int(input())
    graph[a].append(i)

for i in range(1, n+1):
    visited=[False] * (n+1)
