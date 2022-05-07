n = int(input())
arr = list(map(int, input().split()))

sum = [0 for _ in range(n)]
sum[0] = arr[0]

# 누적합
for i in range(1,n):
    sum[i] = sum[i-1] + arr[i]

answer = 0

# 1. 벌-벌-통   ㅁㅇㅇㅁㅇㅇㅇㅂ
for i in range(1,n-1):
    answer = max(answer, 2*sum[n-1] - arr[0] - sum[i] - arr[i])
# 2. 통-벌-벌   ㅂㅇㅇㅁㅇㅇㅇㅁ
for i in range(1, n-1):
    answer = max(answer, sum[n-2] + sum[i-1] - arr[i])
# 3. 벌-통-벌 (i: 통의 위치)   ㅁㅇㅇㅂㅇㅇㅇㅁ
for i in range(1, n-1):    
    answer = max(answer, sum[n-2] - sum[i-1] + sum[i] - arr[0])
print(answer)