W = 1001

N = int(input())
arr = [0] * W

for _ in range(N):
    L, H = map(int,input().split())
    arr[L] = H

left = [0] * W
right = [0] * W

maxLeft = 0
maxRight = 0
for i in range(1, W):
    if arr[i] > maxLeft:
        maxLeft = arr[i]
    left[i] = maxLeft
    
    if arr[W - i] > maxRight:
        maxRight = arr[W - i]
    right[W - i] = maxRight

ans = 0
for i in range(1, W):
    ans += min(left[i], right[i])

print(ans)

# 왼쪽에서, 오른쪽에서부터 선을 그어.
# 두 선 중에서 작은 값이 지붕