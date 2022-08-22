# bc = b*암호의 길이+c의 순서 
# bcb = bc*암호의 길이 + b의 순서 
# bcbb = bcb*암호의길이 + b의 순서
arr = input()
pw = input()


key = arr.find(pw[0]) + 1

for i in range(1,len(pw)):
    idx = arr.find(pw[i])
    # print(i, key, len(arr), idx + 1)
    key = key*len(arr) + (idx + 1)
print(key % 900528)


""" #시간초과#
cnt = 0

#암호가 n가지면 n-1자리까지를 만드는 경우의수
for i in range(1, len(pw)):
    cnt += len(arr) ** i

#마지막자린데... abcdefg beb면 -> ae만드는거까지 했고..
# aaa~agg 하고 그 다음에 b로 시작하는거 해야지
for i, v in enumerate(pw):
    cnt += (arr.find(v)*(len(arr) ** (len(pw)-1-i)))

print((cnt+1) % 900528) """

""" 
최적화 -> 시간초과 안남..!! 
cnt = 0
temp = 1

for i in range (len(pw) - 1, -1, -1) :
    idx = arr.find(pw[i])
    cnt = (cnt + temp * (idx + 1)) % 900528
    temp = temp * len(arr) % 900528

print(cnt) 
"""