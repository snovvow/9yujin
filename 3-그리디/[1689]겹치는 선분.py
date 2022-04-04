# https://peisea0830.tistory.com/63

import sys

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x:x[1])
arr.sort(key=lambda x:x[0])

print(arr)