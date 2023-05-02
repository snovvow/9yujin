import sys

N, M = map(int, input().split())
""" keyword = []
memo = []
for _ in range(N):
    keyword.append(input())
keywordset = set(keyword)
for _ in range(M):
    write = sys.stdin.readline().split(',')
    memo = memo + write
    memoSet = set(memo)
    print(len((keywordset - memoSet))) """

keyword = dict()

for _ in range(N):
    a = sys.stdin.readline().rstrip()
    keyword[a] = 1

ans = N
for _ in range(M):
    write = sys.stdin.readline().rstrip().split(',')
    
    for t in write:
        if t in keyword.keys() and keyword[t] == 1:
            keyword[t] -= 1
            ans -= 1
            
    print(ans)

