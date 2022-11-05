N = int(input())

# N N-1 2 N-3 4 N-5
answer = []

if N == 1:
    print(1)
elif N % 2 == 1:
    print(-1)
else:
    for i in range(N):
        if i == 0:
            answer.append(N)
        elif i % 2 == 1:
            answer.append(N-i)
        else:
            answer.append(i)
    for i in answer:
        print(i,end=" ")
