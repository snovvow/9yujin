from collections import Counter

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 얘도 시간초과...?
ans = 0
start = 0
end = 0

count = [0] * 100001

while end < N -1:
    temp = arr[start:end+1]
    if count[arr[end]] > K:
        count[arr[start]] = count[arr[start]] - 1
        start += 1

        if end < start:
            end += 1
    
    else:
        length = len(temp)
        if length > ans:
            ans = length
        end += 1
        count[arr[end]] = count[arr[end]] + 1

print(ans)

# 시간초과
""" while end < N:
    temp = arr[start:end+1]
    if temp.count(arr[end]) > K:
        start += 1
        if end < start:
            end += 1
    else:
        length = len(temp)
        if length > ans:
            ans = length
        end += 1
        
print(ans) """