# https://tooo1.tistory.com/441

n,k= map(int, input().split())
num = list(input())

# 지울수 있는 개수
count = k

new = []

# 1. 제일 높은 자리수부터 크게 만들기
for i in range(n):
    # 더 지울수 있고, 스택에 값이 있을떄
    while count > 0 and new:

        # 가장 최근에 넣은것(앞자리 숫자)과 현재 인덱스를 비교해서, 
        if new[-1] < num[i]:
            # 앞자리 숫자가 더 작으면 없애버려
            new.pop()
            count -= 1
        else:
            break
    # 아니면, 스택에 앞에서부터 추가
    new.append(num[i])   


# 2. 앞의 수가 다음수보다 작으면 없애버려
# 근데 굳이 1번 2번 안나눠도 됐을듯


print(''.join(new[:n-k]))