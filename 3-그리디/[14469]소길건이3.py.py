n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

# 2차원배열의 0번째인덱스들로 정렬
arr.sort(key=lambda x:x[0])

time = 0

for i in arr:
    if time > i[0]:
        time += i[1]
    else:
        time = i[0] + i[1]

print(time)