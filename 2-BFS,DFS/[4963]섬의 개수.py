# 동빈북 151p 참고
import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    # 범위 벗어났을때
    if  x <= -1 or x >= m or y <= -1 or y >= n:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        graph[x][y] = 2

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        #대각선
        dfs(x+1, y+1)
        dfs(x-1, y-1)
        dfs(x+1, y-1)
        dfs(x-1, y+1)
        return True
    return False

while (1):
    n, m = map(int, input().split())
    if not n and not m:
        break
    graph = []
    for i in range(m):
        graph.append(list(map(int, input().split()))) #붙어있는숫자 배열에 각각넣을때

    result = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                dfs(i,j)
                result += 1
    print(result)