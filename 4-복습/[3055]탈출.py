import sys
from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


r, c = map(int, input().split())
arr = []

visit=[[0]*c for _ in range(r)]
queue = deque()

for _ in range(r):
    arr.append((list(map(str, sys.stdin.readline().rstrip()))))

