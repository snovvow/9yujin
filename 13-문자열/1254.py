s=input()

# 처음부터 펠린드롬이면
if s==s[::-1]:
    print(len(s))

# 아니면
else:
    ln=len(s) + 1 # 끝에 하나 추가하고 시작
        
    for i in range(len(s),0,-1):
        mid=int(ln/2)
        rs=(len(s)-mid)

        # 홀수면, 가운데꺼 제외하고 양 옆 비교
        if ln%2==1 :
            
            # 가운데 기준 왼쪽부터 역순 == 가운데 기준 오른쪽부터 + i개 추가
            if s[-rs-1::-1]==s[mid+1:]+s[-i::-1]:
                print(ln)
                break
            else:
                ln+=1
        # 짝수면, 
        else:
            # 가운데 기준 왼쪽부터 역순 == 가운데 기준 오른쪽부터 + i개 추가
            if s[-rs-1::-1]==s[mid:]+s[-i::-1]:
                print(ln)
                break
            else:
                ln+=1
    else:
        print(2*len(s)-1)


""" s= [1,2,3,4,5]
print(s[3::][::-1])
print(s[3::-1])
print(s[-3::-1]) """
