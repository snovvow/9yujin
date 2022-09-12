from itertools import combinations

def sol():
    flag = 0
    for combItem in comb:
        # 각 경우의 수마다 가능 여부 체크하기
        min = 0
        max = 0
        # 최소 개수만 일단 더한 후에 확인
        for i in combItem:
            min = min + i[0]
            max = max + i[1]
        """ # min이 E면 출력하고 리턴
        if min == E:
            for i in combItem:
                print(i[0], end=' ')
            return """
        # 불가능한 경우 : 다음 반복으로
        if min > E or max < E :
            continue

        left = E - min # 최소개수만큼 주고 남은 인형 수
        get = [] # N명이 각각 받은 인형 개수
        space = [] #N명이 각각 더 받을 수 있는 인형 개수
        for i in combItem:
            get.append([i[0], i[2]]) # 처음에 최소개수만큼 받고 시작함
            space.append(i[1] - i[0])
        for i in range(P):
            # 맨 앞사람부터. 남은 인형이 있고, 최대 개수보다 적게 갖고있을때 하나씩 준다.
   
            if left == 0:
                continue
            if left <= space[i]: # 해당 사람에게 주면 끝나는 경우
                get[i][0] = get[i][0] + left
                left = 0
                space[i] = space[i] - left
            else: # 해당 사람한테 줄만큼 줘도 남는경우
                get[i][0] = get[i][0] + space[i]
                left = left - space[i]
                space[i] = 0
        print(get)
        ans = [0] * N
        for i in get:
            ans[i[1]] = i[0]
        for i in ans:
            print(i, end=' ')
        flag = 1   
        return
    if flag == 0 :
        print(-1)
        
        


# 입력 받기
N, P, E = map(int, input().split())
arr = []

# [최솟값, 최댓값, 원래 N 내에서의 인덱스]
for i in range(N):
    inputValue = list(map(int, input().split()))
    inputValue.append(i)
    arr.append(inputValue)
# 인형을 받을 P명에 대한 경우의 수
comb = list(combinations(arr, P))

sol()