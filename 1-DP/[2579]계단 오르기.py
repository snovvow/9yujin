import sys

n = int(input())
m = []
for i in range(n):
    m.append(int(input()))

d = [0] * n

d[0] = m[0]
if n == 1:
    print(d[0])
    sys.exit(0)

d[1] = m[1]+m[0]
if n == 2:
    print(d[1])
    sys.exit(0)
    
d[2] = max(m[0]+m[2], m[1]+m[2]) 


for i in range(3, n):
    d[i] = max(d[i-2] + m[i], d[i-3] + m[i-1] + m[i])

print(d[n-1])