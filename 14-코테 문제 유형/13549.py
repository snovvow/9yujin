from collections import deque
import sys
n, k = map(int, sys.stdin.readline().split())
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
        #순간이동

        # 걷기
        for j in (x-1, x+1, 2*x):
            if 0 <= j <= max_num and not visited[j]:
                if j == 2*x:
                    visited[j] = visited[x]
                    q.appendleft(j)
                else:
                    visited[j] = visited[x]+1
                    q.append(j)

bfs()