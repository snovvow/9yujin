n,k= map(int, input().split())
number = list(map(int,input()))

# 지울수 있는 개수
count = k

new = number

# 1. 앞에꺼가 뒤에거보다 작으면 없애기
for i in range(n):
    while count > 0:
        if number[i] < number[i+1]:
            new.remove(number[i])
            count -= 1


print(new)