N,K = map(int, input().split())
ans = []
def dfs(value, acc, arr:list):
    
    if acc > N:
        return
    else :
        arr.append(value)
    
    if acc == N:
        ans.append(arr)
        print(ans)
    
    dfs(1, acc+1, arr)
    dfs(2, acc+2, arr)
    dfs(3, acc+3, arr)
dfs(0,0,[])