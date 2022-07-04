arr1 = input()
arr2 = input()

dp = [[0] * (len(arr2)+1) for _ in range(len(arr1)+1)]

for i in range(1, len(arr1)+1):
    for j in range(1, len(arr2)+1):
        if arr1[i-1] == arr2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence