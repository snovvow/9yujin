# https://it-garden.tistory.com/341 참고...

n, k = map(int, input().split())

# 0부터 N 까지의 정수 K개를 더해서 N을 만드는 경우의 수
# k = 1: 1      가지 (N 자신)
# k = 2: n+1    가지
d = [[0] * (n+1) for i in range(k+1)]
for i in range(1, n+1):
    d[1][i] = 1
    if k>1:
        d[2][i] = i+1

# k = 3 : (k=2, n)일 때 가짓수 + (k = 3, n-1)일 때 가짓수
#
# 직접 단위가 작을때의 경우를 세보면서 점화식을 도출해보면 될듯!!!

for i in range(2, k+1):
    d[i][1] = i # 0부터 1까지의 정수 k개를 더해서 1를 만드는 경우의 수 : k개 (1,0,..,0) ~ (0,0,..,1)
    for j in range(2, n+1):
        d[i][j] = d[i-1][j] + d[i][j-1]

print(d[k][n] % 1000000000)