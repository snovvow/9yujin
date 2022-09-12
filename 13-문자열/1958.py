arr1 = input()
arr2 = input()
arr3 = input()

dp = [[[0] * (len(arr3)+1) for _ in range(len(arr2)+1)] for _ in range(len(arr1)+1)]

for i in range(1, len(arr1)+1):
    for j in range(1, len(arr2)+1):
        for k in range(1, len(arr3)+1):
            if arr1[i-1] == arr2[j-1] == arr3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1]+1
            else :
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1], dp[i - 1][j - 1][k], dp[i][j - 1][k - 1], dp[i - 1][j][k - 1])

print(dp[-1][-1][-1])