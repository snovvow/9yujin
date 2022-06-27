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
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

# 입력받아서, union find 해나가기
for i in range(n-2):
    a, b = map(int, sys.stdin.readline().split())
    union(a,b)

# 다시 잇기 부모노드 다른것들을 찾아서 그거끼리 이어
parentSet = []
for i in range(1, n+1):
    parentSet.append(find(i))
parentSet = list(set(parentSet))
print(parentSet[0], parentSet[1])

