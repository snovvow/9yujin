import pprint

N = int(input())
todos = []

# 최대 N칸만큼.. 365개
calender = [[0 for _ in range(N)] for _ in range(366)]
for i in range(N):
    todos.append(list(map(int, input().split())))

todos.sort(key=lambda x: -x[1])
todos.sort(key=lambda x: x[0])

for todo in todos:
    start, end = todo[0], todo[1]
    space = 0

    # 시작위치 잡기
    for i in range(N):
        if calender[start][i] == 0:
            space = i
            calender[start][space] = 1
            break
    # 둘째날부터
    for i in range(start + 1, end + 1):
        calender[i][space] = 1


# 종이 너비 만들고 출력하기
ans = 0
width = 0
height = 0

for i in range(366):
    M = 0

    for j, v in enumerate(calender[i]):
        if v == 1:
            M = j + 1

    if M == 0 or i == 365:
        if i == 365 and M != 0:
            height = max(M, height)
            width += 1

        ans += width * height
        width = 0
        height = 0
        M = 0
    else:
        height = max(M, height)
        width += 1

print(ans)
