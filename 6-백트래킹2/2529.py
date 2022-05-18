import sys
a = int(input())
arr = list(sys.stdin.readline().split())
visited = [0] * 10
max = ""
min = ""

def check(i,j,op):
    if op =='<':
        return i<j
    if op == '>':
        return i>j


def dfs(depth, ans):
    global max, min
    # 정답이라면
    if depth == a + 1:
        if not len(min):
            min = ans
        else:
            max = ans
        return
    # 정답이 아니라면
    else:
        # 뻗을 수 있는 모든 자식 노드에 대해서
        for i in range(10):
            # 정답에 유망하다면
            if not visited[i]:

                if depth == 0 or check(ans[-1], str(i), arr[depth-1]):
                    visited[i] = True
                    dfs(depth + 1, ans + str(i))
                    visited[i] = False

dfs(0, "")
print(max)
print(min)


""" def 재귀함수(depth):

    if 정답이라면? :
        정답 출력 or 저장

    else : 정답이 아니라면?
        for 뻗을 수 있는 모든 자식 노드에 대해서 :
            if 정답에 유망하다면 :
                자식노드로 이동 (방문표시)
                재귀함수(depth+1)
                부모노드로 이동 (방문표시제거)
"""