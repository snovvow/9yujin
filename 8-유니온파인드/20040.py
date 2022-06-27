import sys

def find(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find(parent[x])
    return parent[x]

def union(a, b, turn):
    global end
    a = find(a)
    b = find(b)

    # 사이클 생겼을때
    if a == b:
        if end != 0:
            end = turn + 1
    else :
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

# init
end = 0
n, m = map(int, sys.stdin. readline().split())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

# 입력받아서, union find 해나가기
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b, i)

print(end)