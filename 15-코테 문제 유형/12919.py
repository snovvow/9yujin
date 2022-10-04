S = input()
T = input()
ans = 0
def add(prev):
    return prev + 'A'

def reverse(prev):
    temp = prev + 'B'
    return temp[::-1]

def sol(S,T):
    global ans
    if len(S) == len(T):
        if S == T:
            ans = 1
            return
        else:
            return
    
    sol(add(S),T)
    sol(reverse(S),T)

sol(S,T)
print(ans)