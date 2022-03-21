# https://mong9data.tistory.com/68 참고..

n, k = map(int, input().split())
coin = []

for i in range(n):
    coin.append(int(input()))

d = [0] * (k+1) # d[i] : 합이 i가 되는 경우의 수
d[0] = 1 #d[1] = 0 + 1이 되어야 하는데, 그 1을 여기서 꺼내서 씀

for i in coin:
    for j in range(i, k+1): # 합이 j가 되는 경우(j는 i~k) 메모
        if j-i >= 0:
            d[j] += d[j-i]
print(d[k])