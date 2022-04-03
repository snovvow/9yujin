# https://bbbyung2.tistory.com/67
from collections import deque


n, m = map(int, input().split())

graph = []

#녹일 숫자
add_count = [[0] * m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

day = 0