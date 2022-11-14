import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().split())
board = []
visited = set()
ans = 0


for _ in range(R):
    board.append(list(sys.stdin.readline().rstrip()))


def sol(x, y, depth):
    global ans
    ans = max(ans, depth)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not board[nx][ny] in visited:
            visited.add(board[nx][ny])
            sol(nx,ny, depth + 1)
            visited.remove(board[nx][ny])

visited.add(board[0][0])
sol(0,0,1)
print(ans)

""" def 재귀함수(depth):

    if 정답이라면? :
        정답 출력 or 저장

    else : 정답이 아니라면?
        for 뻗을 수 있는 모든 자식 노드에 대해서 :
            if 정답에 유망하다면 :
                자식노드로 이동 (방문표시)
                재귀함수(depth+1)
                부모노드로 이동 (방문표시제거. 백트래킹한거임)
"""