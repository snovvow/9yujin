# N : 접시 수
# d : 초밥 가짓수
# k : 연속해서 먹는 접시 수
# c : 쿠폰 번호

N, d, k, c = map(int, input().split())
arr = []
ans = 0
for _ in range(N):
    arr.append(input())

for start in range(N):
    eat = set()
    end = start + k

    # 4개씩 집합에 넣는 모든 경우의 수
    for i in range(start, end):
        eat.add(arr[i % N])
    if str(c) not in eat:
        eat.add(c)
    ans = max(ans, len(eat))
print(ans)