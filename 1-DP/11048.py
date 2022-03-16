n,m = map(int, input().split())

array = []
# 메모이제이션 어쩌구..
d = [[0]*(m+1) for i in range(n+1)]

for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(1,n+1):
    for j in range(1,m+1):
        d[i][j] = max(d[i-1][j], d[i-1][j-1], d[i][j-1]) + array[i-1][j-1]

print(d[i][j])