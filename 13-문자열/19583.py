import sys

S, E, Q = input().split()
S = int(S[:2] + S[3:])
E = int(E[:2] + E[3:])
Q = int(Q[:2] + Q[3:])
before = []
after = []
while True:
    try:
        time, nickname = sys.stdin.readline().split()
        time = int(time[:2] + time[3:])
        if time <= S:
            before.append(nickname)
        if time >= E and time <= Q:
            after.append(nickname)
    except:
        break


ans = (set(before) & set(after))
print(len(list(ans)))