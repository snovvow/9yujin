N = int(input())
arr = list(map(int, input().split()))

left = 0
right = N - 1
ans = abs(arr[0] + arr[N-1])
ans_left = left
ans_right = right

while left < right:
    temp = arr[left] + arr[right]

    if abs(temp) < ans:
        ans_left = left
        ans_right = right
        ans = abs(temp)

    if temp < 0:
        left += 1
    elif temp > 0:
        right -= 1
    else:
        break

print(arr[ans_left], arr[ans_right])