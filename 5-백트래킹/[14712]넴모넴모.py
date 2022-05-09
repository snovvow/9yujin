""" 
def 재귀함수(depth):

    if 정답이라면? :
        정답 출력 or 저장

    else : 정답이 아니라면?
        for 뻗을 수 있는 모든 자식 노드에 대해서 :
            if 정답에 유망하다면 :
                자식노드로 이동.. visited = 1
                재귀함수(depth+1)
                부모노드로 이동.. visited = 0 
"""

import pprint

def dfs(count): # count:현재 visit한 노드 개수
    global answer

    # 정답이라면?? -> 마지막 칸까지 다 검사를 했을때.
    if count == n * m:
        answer += 1
    
    else : # 정답이 아니라면?

        # 1234
        # 5678
        # ..뭐 이 순서로 오른쪽으로 순서대로 dfs해나가는것

        y = count // m + 1 # 몫 -> 행
        x = count  % m + 1 # 나머지 -> 열

        # 1. 넴모 안놓고 다음거로 넘어가는 경우
        dfs(count + 1)

        # 2. 네모 넣으려고 하는 경우
        # 왼,왼위, 위 체크 -> 다 1일때 그자리 두면 놓을수없는자리
        if graph[y - 1][x] == 0 or graph[y][x - 1] == 0 or graph[y - 1][x - 1] == 0:
            graph[y][x] = 1
            dfs(count + 1)
            graph[y][x] = 0


n, m = map(int, input().split())
# 1부터 인덱스 시작하도록 함.
graph = [[0]* (m+1) for _ in range(n+1)]
answer = 0

dfs(0)
print(answer)
