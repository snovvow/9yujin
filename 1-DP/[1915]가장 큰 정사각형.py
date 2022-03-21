n, m = map(int, input().split())

arr = []
d = [[0] * m for i in range(n)] 

for i in range(n):
    arr.append(list(map(int, list(input().rstrip()))))

#i,j 0일때는 안건드니까 1부터 탐색..?
for i in range(1, n):
    for j in range(1, m):
        #0일땐 넘어가
        if arr[i][j] == 0:
            continue

        if arr[i-1][j] and arr[i][j-1] and arr[i-1][j-1]:
            # 왼/대각/위의 최솟값에서 +1 하기. 
            # 111
            # 111
            # 123
            # 12
            # 이런경우가 있어서!!
            arr[i][j] = min(arr[i-1][j-1], arr[i][j-1], arr[i-1][j]) + 1

maxnum = max(map(max, arr))
print(maxnum ** 2)