N = int(input())
arr = list(map(int, input().split()))

odd = [0] * (N//2 + 1) #홀수 dp
even = [0] * (N//2 + 1) #짝수 dp

#기본상태 누적합
for i in range(1,N+1):
    if i % 2 == 1:
        odd[i//2 +1] = (odd[i//2] + arr[i-1])
    if i % 2 == 0:
        even[i//2] = (even[i//2 -1] + arr[i-1])

# 밑장 안뺐을때 상태를 이니셜로 두고 얘랑 비교하나가는거야
ans = odd[N//2]

#내차례에서 밑장뺄때
for i in range(N//2):
    temp = odd[i+1] + even[N//2] - even[i+1]
    ans = max(ans, temp)


#상대방 차례에서 밑장뺄때
for i in range(N//2):
    temp = odd[i+1] + even[N//2 -1] - even[i]
    ans = max(ans, temp)

print(ans)