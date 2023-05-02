dx = [1, 1, 1, 0]
dy = [-1, 0, 1, 1]


def find(x, y):
    color = graph[x][y]

    for i in range(4):
        count = 1
        nx = x + dx[i]
        ny = y + dy[i]

        while 0 <= nx < 19 and 0 < ny < 19 and graph[nx][ny] == color:
            count += 1

            # 오목 됐을때
            if count == 5:
                if (
                    0 <= x - dx[i] < 19
                    and 0 <= y - dy[i] < 19
                    and graph[x - dx[i]][y - dy[i]] == color
                ):
                    break
                if (
                    0 <= nx + dx[i] < 19
                    and 0 <= ny + dy[i] < 19
                    and graph[nx + dx[i]][ny + dy[i]] == color
                ):
                    break
                print(color)
                print(x + 1, y + 1)
                exit(0)
            nx += dx[i]
            ny += dy[i]


graph = []
for i in range(19):
    graph.append(list(map(int, input().split())))

for i in range(19):
    for j in range(19):
        if graph[i][j] != 0:
            find(i, j)
print(0)


## 맞왜틀
