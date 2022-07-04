import re

t = int(input())

for i in range(t):
    a = input()
    ans = re.compile('(100+1+|01)+')

    if ans.fullmatch(a):
        print('YES')
    else:
        print('NO')