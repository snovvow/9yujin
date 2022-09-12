N, K, B = map(int, input().split())

arr = [0] * (N+1)

# 망가진 신호등 : 1
# 정상 신호등 : 0
for i in range(B):
    broken = int(input())
    arr[broken] = 1

for i in range(1,N+1):
    arr[i] += arr[i-1]

# 0 0 0 0 0 0 0 0 0 0
# 1 1 0 0 1 0 0 1 0 1
# 1 2 2 2 3 3 3 4 4 5

# 16번째줄에서 i ~ i+5 까지 6개가 되기 위해 고쳐야하는 신호등 수 :
# arr[i+5] - arr[i]

MIN = 0
for i in range(N-K+1):
    ans = arr[i+K-1]
    if i == 0:
        MIN = ans
    else :
        ans -= arr[i-1]
        MIN = min(ans, MIN)

print(MIN)