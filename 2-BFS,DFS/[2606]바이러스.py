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