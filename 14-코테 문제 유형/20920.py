import sys
from collections import Counter

N, M = map(int,input().split())
arr = []

for _ in range(N):
    text = sys.stdin.readline().rstrip()
    # 길이가 M 이상인거만 집어넣어
    if  len(text) >= M:
        arr.append(text)


res = Counter(arr).most_common()
# print(res).. 개사기네.
# [('sand', 3), ('apple', 2), ('append', 1)]

res.sort(key = lambda x : (-x[1], -len(x[0]), x[0]))
# 저걸 정렬을 할건데, 
# -x[1] : 개수를 가지고 내림차순
# -len[x[0]] : 길이를 가지고 내림차순
# ㅌ[0] : 알파벳순
for r in res :
    print(r[0])
    