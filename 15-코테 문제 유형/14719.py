#위에서부터 깎기

H, W = map(int, input().split())
X = list(map(int, input().split()))
high = max(X)
low = min(X)
ans = 0
for i in range(high, low, -1):
    Y = [0] * W
    
    for j in range(W):
        if X[j] >= i:
            Y[j] = 1
    
    sum = 0
    tempSum = 0
    flag = 0
    print(Y)
    for j in range(W):
        # 1이면 flag : true
        if Y[j] ==1:
            flag = 1
            sum += tempSum
            tempSum = 0
        # 0이고, 맨 끝이 아니면
        elif j != W-1:
            if flag == 1:
                tempSum += 1
        # 0이고 맨 끝이면
        else:
            tempSum = 0
    ans += sum
print(ans)