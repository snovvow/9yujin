import sys
a = int(input())
arr = list(sys.stdin.readline().split())
visited = [0] * a

def check(i,j,op):
    if op =='<':
        return i<j
    if op == '>':
        return i>j




""" def 재귀함수(depth):

    if 정답이라면? :
        정답 출력 or 저장

    else : 정답이 아니라면?
        for 뻗을 수 있는 모든 자식 노드에 대해서 :
            if 정답에 유망하다면 :
                자식노드로 이동
                재귀함수(depth+1)
                부모노드로 이동 """