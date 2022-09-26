from collections import deque

n, k = map(int, input().split())
max_num = 100000
visited = [0] * (max_num + 1) #인덱스 1부터 맞추기

def bfs():
    q = deque()
    # 첫 출발점
    q.append(n)
    while q:
        x = q.popleft()
        if x==k:
            print(visited[x])
            break
        
        # 이동할 수 있는 모든 방향
        for j in (x-1, x+1, x*2):
            if 0 <= j <= max_num and not visited[j]:
                visited[j] = visited[x]+1
                q.append(j)
bfs()