N, S = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
sum = arr[0]
ans = 100001
while 1:
    # 합이 S보다 클때
    if sum >= S:
        sum -= arr[left]
        ans = min(ans, right-left+1)
        left += 1
    else :
    # S보다 작을때 : 윈도우 늘려
        right += 1
        if right == N:
            break
        sum += arr[right]


print(0) if ans == 100001 else print(ans)
