import sys

T = int(input())

for _ in range(T):
    N = int(sys.stdin.readline())
    cost = list(map(int, sys.stdin.readline().split()))
    
    ans = 0
    max = cost[-1]
    #start, stop, step
    for i in range(N-1,-1,-1):
        if cost[i] > max:
            max = cost[i]
        else:
            ans += max - cost[i]
    print(ans)