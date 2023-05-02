from itertools import combinations

N,M = map(int, input().split())

home = []
chickens = []

for i in range(N):
    row = list(map(int, input().split()))
    for index in range(len(row)):
        if row[index] == 1:
            home.append([i,index])
        if row[index] == 2:
            chickens.append([i,index])

answer = 9999
for chicken in combinations(chickens,M):
    total = 0
    for i in home:
        distance = 9999
        for j in chicken:
            distance = min(distance, abs(j[0]-i[0])+abs(j[1]-i[1]))
        total += distance
    answer = min(answer, total)
print(answer)