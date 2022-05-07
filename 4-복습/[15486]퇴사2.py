import sys

n = int(input())
arr= []
dp = [0] * 1500001

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))


for i in range(n):
    # i번째날에 잡혀있는 상담이 퇴사 전에 끝나는거면(가능한거면),
    if i + arr[i][0] <= n: 

        # i번째날 수익 + 그날 상담한거 결과 or 
        # 그냥 내비둬(원래거가 더 크면 : 다른날에 시작한 상담 누적이 더 비싼거면)
        dp[i + arr[i][0]] = max(dp[i] + arr[i][1], dp[i + arr[i][0]])
    
    # 그 다음날꺼는 그 전날꺼에서 누적해야되니까
    dp[i+1] = max(dp[i+1], dp[i])

print(max(dp))