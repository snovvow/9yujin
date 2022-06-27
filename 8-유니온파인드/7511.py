import sys

testcase = int(input())

for test in range(1, testcase+1):
    print("Scenario :",test)
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
    k = int(input())
    parent = [0] * (n+1)

    for i in range(1, n+1):
        parent[i] = i

    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        union(a,b)

    m = int(input())
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if find(a) == find(b):
            print('1')
        else:
            print('0')
    if test <testcase:
        print('\n')