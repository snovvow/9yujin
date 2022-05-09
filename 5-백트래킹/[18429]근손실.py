n,k = map(int,input().split())
arr = list((map(int, input().split())))
visited = [0] * n
answer = 0

def dfs(depth, weight):
    if depth >= n:
        global answer
        answer += 1
    else:
        for i in range(n):
            if visited[i]==0:
                if weight+ arr[i] - k >= 0:
                    visited[i] = 1
                    dfs(depth+1, weight + arr[i]-k)
                    visited[i] = 0


dfs(0,0)
print(answer)

#213
#231
#312
#321
#---백트래킹 특---
# https://moz1e.tistory.com/15

""" def 재귀함수(depth):

    if 정답이라면? :
        정답 출력 or 저장

    else : 정답이 아니라면?
        for 뻗을 수 있는 모든 자식 노드에 대해서 :
            if 정답에 유망하다면 :
                자식노드로 이동
                재귀함수(depth+1)
                부모노드로 이동 """