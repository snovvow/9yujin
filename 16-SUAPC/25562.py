
N = int(input())
print(N*(N-1) // 2)
number = 1
for _ in range(N):
    print(number, end=' ')
    number *= 2
print()
print(N-1)
number = 1
for _ in range(N):
    print(number, end=' ')
    number += 1