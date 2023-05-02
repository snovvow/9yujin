A, B = map(int, input().split())
N, M = map(int, input().split())

robots = []
commands = []

for _ in range(N):
    x, y, d = input().split()
    robots.append([int(x), int(y), d])

for _ in range(M):
    robot, command, count = input().split()
    commands.append([int(robot), command, int(count)])

print(robots, commands)


def L(robot):
    robots[robot - 1][2]


for i in commands:
    robot = i[0]
