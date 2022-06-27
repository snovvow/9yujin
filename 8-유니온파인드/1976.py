import sys

def find(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# init
n = int(input())
m = int(input())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(1, n+1):
        arr = list(map(int, sys.stdin.readline().split()))

        for j in range(1, n+1):
            if arr[j-1] == 1:
                union(i,j)

plan = list(map(int, sys.stdin.readline().split()))
parentSet = []

for i in plan:
    parentSet.append(find(i))
parentSet = list(set(parentSet))

if len(parentSet) == 1:
    print("YES")
else:
    print("NO")


